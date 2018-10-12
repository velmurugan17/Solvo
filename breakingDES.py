# DES has a fixed block size of 32 byte and its key are 64 bit long
# Performance analysis : https://www.cse.wustl.edu/~jain/cse567-06/ftp/encryption_perf/
# https://www.programcreek.com/python/example/101304/Crypto.Cipher.DES.MODE_ECB
# https://www.dlitz.net/software/pycrypto/api/current/Crypto.Cipher.DES-module.html
# 2**55
# print(2**55)
import time
from datetime import datetime, timedelta
from Crypto.Cipher import DES
from Crypto import Random
iv=Random.get_random_bytes(8)

def runtime(func):
    def wrapper(*args):
        st =time.time()
        result = func(*args)
        et = time.time()
        t=et-st
        print(t)
        return t,result
    return wrapper

@runtime
def encrypt(text,key):
    """

    :param text:
    :param key:
    :return:
    """
    des1=DES.new(key,DES.MODE_OFB,iv)
    cipher_text = des1.encrypt(text)
    return cipher_text

@runtime
def decrypt(ctext,key):
    """

    :param ctext:
    :param key:
    :return:
    """
    des2=DES.new(key,DES.MODE_OFB,iv)
    plain_text = des2.decrypt(ctext)
    return plain_text
text='32 byte plain text data for test'
print(len(text.encode('utf-8')))

def measureIt(t):
    d=t*2**55
    print(d)
    print(d/(60*60*24))
    # d = timedelta(t*2**55)
    # d_time = datetime(1,1,1)+d
    # print("%d:%d:%d:%d" % (d_time.day - 1, d_time.hour, d_time.minute, d_time.second))

encrypt_time,ctxt = encrypt(text,'abcdefgh')
decrypt_time,ptxt = decrypt(ctxt,'abcdefgh')
print(decrypt_time)
measureIt(decrypt_time)
