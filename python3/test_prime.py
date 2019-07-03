from math import sqrt
from time import time


def is_prime(n):
    if n <= 1:
        return False
    if n != 2 and n % 2 == 0:
        return False
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


# sieve of eratosthenes
def find_primes(start, end):
    sieve = [True] * (end + 1)
    for i in range(3, int(sqrt(end)) + 1, 2):
        if not sieve[i]:
            continue
        for j in range(i * 2, end + 1, i):
            sieve[j] = False
    prime = []
    if start <= 2 and end >= 2:
        prime.append(2)
    for i in range(3, len(sieve), 2):
        if sieve[i] == True and i >= start:
            prime.append(i)
    return prime


def test():
    assert is_prime(32416190071) == True
    assert is_prime(4) == False
    assert find_primes(1, 10) == [2, 3, 5, 7]


if __name__ == '__main__':
    start = time()
    test()
    print("Execution time:", time() - start)
