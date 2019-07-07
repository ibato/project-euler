from time import time
from math import sqrt
import test_prime as prime
import test_runner as runner

sieve = prime.find_primes(2, 1000)


def solve():
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
    return answer


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


def test():
    right_answer = 134043
    runner.run(solve, right_answer)


if __name__ == '__main__':
    test()
