from time import time
import test_combinatorics as combinatorics
import test_runner as runner

# 015. Lattice paths
# https://projecteuler.net/problem=15


def solve():
    return combinatorics.nCr(40, 20)


def test():
    right_answer = 137846528820
    runner.run(solve, right_answer)


if __name__ == '__main__':
    test()
