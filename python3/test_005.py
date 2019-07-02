from time import time
import test_runner as runner

# 005. Smallest multiple
# https://projecteuler.net/problem=5


# From 1 to 20:
# - 16 is the largest number that has most 2's as the factor.
# - 9 is the largest number that has most 3's as the factor.
# - 5 is the largest number that has ...
#   ...
# - 19 is the largest number that has most 19's as the factor.
#
# That's why the answer is 16 * 9 * 5 * 7 * 11 * 13 * 17 * 19
def solve():
    return 16 * 9 * 5 * 7 * 11 * 13 * 17 * 19


def test():
    right_answer = 232792560
    runner.run(solve, right_answer)


if __name__ == '__main__':
    test()
