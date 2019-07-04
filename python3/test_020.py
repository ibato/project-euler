from time import time
from math import factorial
import test_runner as runner

# 020. Factorial digit sum
# https://projecteuler.net/problem=20


def solve():
    return sum([int(x) for x in str(factorial(100))])


def test():
    right_answer = 648
    runner.run(solve, right_answer)


if __name__ == '__main__':
    test()
