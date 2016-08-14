from time import *
from prime import *

start = time()
c = 1000
maximum = 0
answer = 0
prime = acquire_primes(1, c)
for a in range(-c + 1, c):
    for b in prime:
        n = 1
        while True:
            if n * n + a * n + b <= 0: break
            if is_prime(n * n + a * n + b) == False: break
            n = n + 1
        if maximum < n:
            maximum = n
            answer = a * b
end = time()
print answer, end - start
