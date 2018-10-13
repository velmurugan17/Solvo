"""
Thanks for the below sources
https://www.dlitz.net/software/pycrypto/api/current/Crypto.Cipher.DES-module.html
https://www.laurentluce.com/posts/python-and-cryptography-with-pycrypto/

Gone through lot of various resources in google to understand the decryption time performance per second.None of the
https://crypto.stackexchange.com/questions/39923/how-to-calculate-time-taken-by-encryption gave some insight of variant attribute in decryption time in terms of processor,speed,data size and algorithm.
However I ended up implementing with time module to measure the time performance in an executed environment.But its not or very close to static.In each execution the time is dynamic.Hence the decryption time is calculated based on 100 different runtime with same plaintext and key

OUTPUT:
Total number of decryption per second :  56186.25586068318
Time required for 2**55 decryption is approximately 7421743 days
"""

import time
import platform
from Crypto.Cipher import DES
from Crypto import Random

iv = Random.get_random_bytes(8)


# test_plain_text = """The Data Encryption Standard (DES /ˌdiːˌiːˈɛs, dɛz/) is a symmetric-key algorithm for the encryption of electronic data. Although insecure, it was highly influential in the advancement of modern cryptography.
#
# Developed in the early 1970s at IBM and based on an earlier design by Horst Feistel, the algorithm was submitted to the National Bureau of Standards (NBS) following the agency's invitation to propose a candidate for the protection of sensitive, unclassified electronic government data. In 1976, after consultation with the National Security Agency (NSA), the NBS eventually selected a slightly modified version (strengthened against differential cryptanalysis, but weakened against brute-force attacks), which was published as an official Federal Information Processing Standard (FIPS) for the United States in 1977.
#
# The publication of an NSA-approved encryption standard simultaneously resulted in its quick international adoption and widespread academic scrutiny. Controversies arose out of classified design elements, a relatively short key length of the symmetric-key block cipher design, and the involvement of the NSA, nourishing suspicions about a backdoor. Today it is known that the S-boxes that had raised those suspicions were in fact designed by the NSA to actually remove a backdoor they secretly knew (differential cryptanalysis). However, the NSA also ensured that the key size was drastically reduced such that they could break it by brute force attack.[2] The intense academic scrutiny the algorithm received over time led to the modern understanding of block ciphers and their cryptanalysis.
#
# DES is insecure. This is mainly due to the 56-bit key size being too small. In January 1999, distributed.net and the Electronic Frontier Foundation collaborated to publicly break a DES key in 22 hours and 15 minutes (see chronology). There are also some analytical results which demonstrate theoretical weaknesses in the cipher, although they are infeasible to mount in practice. The algorithm is believed to be practically secure in the form of Triple DES, although there are theoretical attacks. This cipher has been superseded by the Advanced Encryption Standard (AES). Furthermore, DES has been withdrawn as a standard by the National Institute of Standards and Technology."""


def runtime(func):
    def wrapper(*args):
        st = time.time()
        result = func(*args)
        et = time.time()
        t = (et - st)
        return t, result

    return wrapper


@runtime
def encrypt(text, key):
    """

    :param text:
    :param key:
    :return:
    """
    des1 = DES.new(key, DES.MODE_OFB, iv)
    cipher_text = des1.encrypt(text)
    return cipher_text


@runtime
def decrypt(ctext, key):
    """

    :param ctext:
    :param key:
    :return:
    """
    des2 = DES.new(key, DES.MODE_OFB, iv)
    plain_text = des2.decrypt(ctext)
    return plain_text


text = '32byte length plain text for tst'
key = 'abcd1234'
time_sample = []


def measureIt(t):
    num_of_decryption_per_sec = 1 / t
    print("Total number of decryption per second : ", num_of_decryption_per_sec)
    time_req_for_given_trans = 2 ** 55 / num_of_decryption_per_sec
    print("Time required for 2**55 decryption is approximately {} days ".format(
        round(time_req_for_given_trans / (60 * 60 * 24))))


# for i in range(0, len(test_plain_text), 32):
#     pt = test_plain_text[i:i + 32]
#     if len(pt) % 32 != 0:
#         break
#     else:
#         # key = pt[:8]
#         key = "abcdefgh"
#         print(len(pt))
#         etime,etext = encrypt(pt,key)
#         dtime,dtext = decrypt(etext,key)
#         time_sample.append(time_sample)


for i in range(100):
    encrypt_time, ctext = encrypt(text, key)
    decrypt_time, ptext = decrypt(ctext, key)
    time_sample.append(decrypt_time)
avg_time_to_decrypt = sum(time_sample) / len(time_sample)
measureIt(avg_time_to_decrypt)
