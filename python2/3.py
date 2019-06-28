from math import *
from time import *
from prime import *

# all numbers
start = time()
n = 600851475143
answer = 0
for i in range(int(sqrt(n)), 2, -1):
    if is_prime(i) == True and n % i == 0:
        answer = i
        break
end = time()
print answer, end - start

# end with 1, 3, 7, 9
start = time()
n = 600851475143
answer = 0
for i in range(int(sqrt(n)), 2, -1):
    if i % 2 == 0 or i % 5 == 0:
        continue
    if is_prime(i) == True and n % i == 0:
        answer = i
        break
end = time()
print answer, end - start

# new...
start = time()
n = 600851475143
answer = 0
for i in range(3, int(sqrt(n)), 2):
    if n % i == 0:
        answer = i
        n = n / i
        i = i - 2
end = time()
print answer, end - start
