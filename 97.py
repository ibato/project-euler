from time import *

start = time()
num = 28433
for i in range(7830457 / 2):
    num = (num * 4) % 10000000000
num = (num * 2 + 1) % 10000000000
end = time()
print num, end - start
