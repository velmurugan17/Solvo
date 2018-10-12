# DES has a fixed block size of 32 byte and its key are 64 bit long
# Performance analysis : https://www.cse.wustl.edu/~jain/cse567-06/ftp/encryption_perf/
# https://www.programcreek.com/python/example/101304/Crypto.Cipher.DES.MODE_ECB
# https://www.dlitz.net/software/pycrypto/api/current/Crypto.Cipher.DES-module.html
# 2**55
# print(2**55)
import platform
print(platform.processor())