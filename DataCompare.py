from pyspark.sql import DataFrameReader
from pyspark.sql import SQLContext
from pyspark import SparkContext

sc = SparkContext(appName='compareTable')
sqlContext = SQLContext(sc)


def get_df_from_parquet(parquet_path=None):
    if not parquet_path:
        parquet_path = 'input-parquet'
    df = sqlContext.read.parquet(parquet_path)
    return df


def get_df_from_psql(host=None, port=None, db=None, table=None, user=None, password=None):
    host = 'localhost'
    port = '5432'
    db = 'testdb2'
    table = 'Orders'
    user = 'postgres'
    password = 'velu123'

    url = 'postgresql://{}:{}/{}'.format(host, port, db)
    properties = {'user': user, 'password': password, "driver": "org.postgresql.Driver"}
    df = DataFrameReader(sqlContext).jdbc(url='jdbc:%s' % url, table=table, properties=properties)
    return df


def get_diff_dataframe(df1, df2):
    df = df1.subtract(df2)
    if df.count() == 0:
        print("The datas are identical")
        return
    return df


df1 = get_df_from_parquet()
df2 = get_df_from_psql()
df = get_diff_dataframe(df1, df2)
if df != None:
    df.show()
