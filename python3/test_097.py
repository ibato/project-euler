from time import time
import test_matrix as matrix
import test_file as file
import test_runner as runner


def solve():
    num = 28433
    for i in range(int(7830457 / 2)):
        num = (num * 4) % 10000000000
    num = (num * 2 + 1) % 10000000000
    return num


def test():
    right_answer = 8739992577
    runner.run(solve, right_answer)


if __name__ == '__main__':
    test()
