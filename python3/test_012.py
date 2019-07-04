from time import time
from math import sqrt
import test_runner as runner

# 012. Highly divisible triangular number
# https://projecteuler.net/problem=12


def solve():
    n = 1
    answer = 0
    while True:
        triangle = n * (n + 1) / 2
        count = 0
        for i in range(1, int(sqrt(triangle)) + 1):
            if triangle % i == 0:
                count = count + 1
        if count * 2 > 500:
            answer = triangle
            break
        n = n + 1
    return answer


def test():
    right_answer = 76576500
    runner.run(solve, right_answer)


if __name__ == '__main__':
    test()
