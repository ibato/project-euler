from time import *
from math import *
from prime import *

def has_four_distinct_prime_factors(n):
    count = 0
    for i in range(len(sieve)):
        if n % sieve[i] == 0:
            count = count + 1
            while n % sieve[i] == 0:
                n = n / sieve[i]
        if n == 1:
            break
    if count == 4:
        return True
    return False

start = time()
sieve = acquire_primes(2, 1000)
answer = 0
consecutive = 0
n = 2 * 3 * 5 * 7
while True:
    if has_four_distinct_prime_factors(n):
        consecutive = consecutive + 1
        if consecutive == 4:
            answer = n - 3
            break
    else:
        consecutive = 0
    n = n + 1
end = time()
print answer, end - start
