from time import *
from prime import *

# 2
start = time()
num_of_primes = 3
current_prime = 9
n = 2
while float(num_of_primes) / float(4 * n - 3) >= 0.1:
    n = n + 1
    for i in range(4):
        if is_prime(current_prime):
            num_of_primes = num_of_primes + 1
        current_prime = current_prime + 2 * (n - 1)
end = time()
print 2 * n - 1, end - start

# 1
start = time()
n = 1
num_of_primes = 0
while True:
    num_of_primes = num_of_primes + len(filter(is_prime, [4 * n * n - 2 * n + 1, 4 * n * n + 1, 4 * n * n + 2 * n + 1]))
    total = 1 + 4 * n
    ratio = float(num_of_primes) / float(total) 
    if ratio < 0.1:
        break
    n = n + 1
end = time()
print 2 * (n + 1) - 1, end - start
