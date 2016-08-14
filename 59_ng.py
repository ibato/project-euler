from time import *
from itertools import *

start = time()
answer = 0
c = [chr(x) for x in range(97, 123)]
f = open("textfiles/cipher1.txt", "r")
encrypted = f.readline().strip().split(",")
for each in product(c, repeat = 3):
    decrypted = ""
    for i in range(len(encrypted)):
        d = int(encrypted[i]) ^ ord(each[i % 3])
        decrypted = decrypted + chr(d)
    if not decrypted.find('the') == -1 and decrypted.find(' ') != -1 and decrypted.find(' a ') != -1 and decrypted.find('.') != -1:
        answer = sum([ord(decrypted[i]) for i in range(len(decrypted))])
        break
f.close()
end = time()
print answer, end - start
