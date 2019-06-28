from math import *
from time import *

def is_prime(n):
    if n <= 1:
        return False
    if n != 2 and n % 2 == 0:
        return False
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def acquire_primes(start, end):
    sieve = [True] * (end + 1)
    for i in range(3, int(sqrt(end)) + 1, 2):
        if not sieve[i]: continue
        for j in range(i * 2, end + 1, i):
            sieve[j] = False
    prime = []
    if start <= 2 and end >= 2:
        prime.append(2)
    for i in range(3, len(sieve), 2):
        if sieve[i] == True and i >= start:
            prime.append(i)
    return prime
