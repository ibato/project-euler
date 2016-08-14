from prime import *
from time import *
from itertools import *

start = time()
answer = 0
num = 1000000

primes = acquire_primes(1, num)
summation = 0
count = 0
for i in range(len(primes)):
    summation = summation + primes[i]
    count = count + 1
    if (summation + primes[i + 1] >= num):
        break

for i in range(count, 1, -1):
    for j in range(num - i):
        s = reduce(lambda x, y: x + y, primes[j:j + i])
        if s > num: 
            break
        if is_prime(s):
            answer = s
            break
    if answer != 0:
        break

end = time()
print answer, end - start
