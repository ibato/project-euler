from time import time
import test_runner as runner


def solve():
    summation = 0
    for i in range(1, 1001):
        summation = summation + pow(i, i)
    divisor = pow(10, 10)
    return summation % divisor


def test():
    right_answer = 9110846700
    runner.run(solve, right_answer)


if __name__ == '__main__':
    test()
