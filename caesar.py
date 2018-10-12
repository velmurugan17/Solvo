"""
Ceasr cipher algorithm
"""
msg = "kbslrpfknrfbqbwmxpbqobebobru"
max_siz = 26
"""
Key 3 : nevousinquietezpasetrehereux => ne vous inquietez pas etre heureux => dont worry be happy
"""

def translate_msg(k,msg):
    trns = ''
    for c in msg:
        if c.isalpha():
            num = ord(c)
            num+=k

            if c.isupper():
                if num>ord('Z'):
                    num-=26
                elif num<ord('A'):
                    num-=26
            elif c.islower():
                if num>ord('z'):
                    num-=26
                elif num<ord('a'):
                    num+=26
            trns+=chr(num)
        else:
            trns+=c
    return trns

for i in range(1,max_siz):
    print('Key : {} Translation : {}'.format(i,translate_msg(i,msg)))

