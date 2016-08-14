from time import *
from math import *
from divisor import *

start = time()
n = 28123
abundant = filter(lambda i: acquire_sum_of_proper_divisors(i) > i, range(12, n + 1))
sieve = [False] * (n + 1)
for i in range(len(abundant)):
    for j in range(i, len(abundant)):
        if abundant[i] + abundant[j] <= n:
            sieve[abundant[i] + abundant[j]] = True
        else:
            break
answer = sum(filter(lambda x: sieve[x] == False, range(1, n + 1)))
end = time()
print answer, end - start
