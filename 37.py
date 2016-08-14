from time import *
from prime import *

def is_right_truncatable_primes(p):
    if isinstance(p, str) == False:
        p = str(p)
    for i in range(len(p)):
        if is_prime(int(p[i::])) == False:
            return False
    return True

def is_left_truncatable_primes(p):
    if isinstance(p, str) == False:
        p = str(p)
    for i in range(1, len(p)):
        if is_prime(int(p[0 : i])) == False:
            return False
    return True

start = time()
answer = 0
count = 0
n = 7
while count < 11:
    n = n + 2
    if '4' in str(n) or '6' in str(n) or '8' in str(n):
        continue
    if is_right_truncatable_primes(n) == True and is_left_truncatable_primes(n) == True:
        print n, 
        answer = answer + n
        count = count + 1
end = time()
print answer, end - start
