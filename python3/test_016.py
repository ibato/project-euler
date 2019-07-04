from time import time
from functools import reduce
import test_runner as runner

# 016. Power digit sum
# https://projecteuler.net/problem=16


def solve():
    return reduce(int.__add__, map(int, str(2 ** 1000)))


def test():
    right_answer = 1366
    runner.run(solve, right_answer)


if __name__ == '__main__':
    test()
