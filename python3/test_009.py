from time import time
from math import sqrt
from functools import reduce
import test_prime as prime
import test_runner as runner

# 009. Special Pythagorean triplet
# https://projecteuler.net/problem=9


# This is just the brute force attack.
def solve():
    for a in range(3, 1000):
        for b in range(4, 1000):
            c = sqrt(a * a + b * b)
            if c == int(c) and a + b + c == 1000:
                return a * b * c
    return -1


def test():
    right_answer = 31875000
    runner.run(solve, right_answer)


if __name__ == '__main__':
    test()
