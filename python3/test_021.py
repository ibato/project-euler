from time import time
from math import factorial
import test_divisor as divisor
import test_runner as runner

# 021. Amicable numbers
# https://projecteuler.net/problem=21


def solve():
    answer = 0
    for i in range(1, 10000):
        sum1 = divisor.get_sum_of_proper_divisors(i)
        sum2 = divisor.get_sum_of_proper_divisors(sum1)
        if (i == sum2) and (i < sum1):
            answer = answer + i + sum1
    return answer


def test():
    right_answer = 31626
    runner.run(solve, right_answer)


if __name__ == '__main__':
    test()
