from time import *
from prime import *

start = time()
n = 1000000
primes = acquire_primes(1, n)
answer = 1
for prime in primes:
    p = str(prime)
    if '0' in p or '2' in p or '4' in p or '6' in p or '8' in p:
        continue
    for i in range(len(p)):
        t = p[i:] + p[0:i]
        if is_prime(int(t)) == False:
            break
    else:
        answer = answer + 1
end = time()
print answer, end - start
