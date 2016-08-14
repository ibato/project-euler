from time import *
from prime import *

# sieve of eratosthenes v1.0
start = time()
n = 2000000
answer = 0
sieve = []

for i in range(n + 1):
    if i % 2 == 0: 
        sieve.append(False);
    else: 
        sieve.append(True);

sieve[1] = False
sieve[2] = True

for i in range(3, int(sqrt(n)) + 1, 2):
    if sieve[i] == True and is_prime(i) == True:
        for j in range(i * 2, n + 1, i):
            sieve[j] = False

for i in range(1, n + 1):
    if sieve[i] == True:
        answer = answer + i

end = time()
print answer, end - start

# sieve of eratosthenes v1.1
start = time()
n = 2000000
sieve = []

for i in range(3, int(sqrt(n)) + 1, 2):
    if is_prime(i) == True:
        for j in range(i * 2, n + 1, i):
            if j % 2 != 0:
                sieve.append(j)

answer = 0
sieveSet = set(sieve)

for i in range(len(sieveSet)):
    answer = answer + sieveSet.pop()

end = time()
print (n / 2) * (n / 2) - answer - 1 + 2, end - start

# sieve of eratosthenes v1.2
start = time()
n = 2000000
sieve = [True] * (n + 1)

for i in range(3, int(sqrt(n)) + 1, 2):
    if is_prime(i) == True:
        for j in range(i * 2, n + 1, i):
            sieve[j] = False

answer = 0
for i in range(len(sieve)):
    if i % 2 != 0 and sieve[i] == True:
        answer = answer + i

end = time()
print answer + 2 - 1, end - start

# sieve of eratosthenes v1.3
start = time()
n = 2000000
sieve = [True] * (n + 1)

for i in range(3, int(sqrt(n)) + 1, 2):
    if is_prime(i) == True:
        for j in range(i * 2, n + 1, i):
            sieve[j] = False

answer = 0
for i in range(3, len(sieve), 2):
    if sieve[i] == True:
        answer = answer + i

end = time()
print answer + 2, end - start

# sieve of eratosthenes v1.4
start = time()
n = 2000000
sieve = [True] * (n + 1)

for i in range(3, int(sqrt(n)) + 1, 2):
    if not sieve[i]: continue
    for j in range(i * 2, n + 1, i):
        sieve[j] = False

answer = 0
for i in range(3, len(sieve), 2):
    if sieve[i] == True:
        answer = answer + i

end = time()
print answer + 2, end - start

# sieve of eratosthenes v1.5
start = time()
answer = reduce(lambda x, y: x + y, acquire_primes(1, 2000000))
end = time()
print answer, end - start
