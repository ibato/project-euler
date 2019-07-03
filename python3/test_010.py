from time import time
from functools import reduce
import test_prime as prime
import test_runner as runner

# 010. Summation of primes
# https://projecteuler.net/problem=10


def solve():
    return reduce(lambda x, y: x + y, prime.find_primes(1, 2000000))


def test():
    right_answer = 142913828922
    runner.run(solve, right_answer)


if __name__ == '__main__':
    test()
