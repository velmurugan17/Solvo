"""

OUTPUT:
Plaintext length 32
Ciphertext length 32
Total number of decryption per second :  44620.255319148935
Time required for 2**55 decryption is approximately 9345531 days
"""


# DES has a fixed block size of 32 byte and its key are 64 bit long
# Performance analysis : https://www.cse.wustl.edu/~jain/cse567-06/ftp/encryption_perf/
# https://www.programcreek.com/python/example/101304/Crypto.Cipher.DES.MODE_ECB
# https://www.dlitz.net/software/pycrypto/api/current/Crypto.Cipher.DES-module.html
# 2**55
# print(2**55)
import time
from Crypto.Cipher import DES
from Crypto import Random
iv=Random.get_random_bytes(8)

def runtime(func):
    def wrapper(*args):
        st =time.time()
        result = func(*args)
        et = time.time()
        t=(et-st)
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
text='32byte length plain text for tst'

def measureIt(t):
    num_of_decryption_per_sec = 1/t
    print("Total number of decryption per second : ",num_of_decryption_per_sec)
    time_req_for_given_trans = 2**55/num_of_decryption_per_sec
    print("Time required for 2**55 decryption is approximately {} days ".format(round(time_req_for_given_trans/(60*60*24))))

encrypt_time,ctxt = encrypt(text,'abcdefgh')
decrypt_time,ptxt = decrypt(ctxt,'abcdefgh')
print("Plaintext length {}".format(len(text.encode('utf-8'))))
print("Ciphertext length {}".format(len(ctxt)))
measureIt(decrypt_time)
