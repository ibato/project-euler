from time import time
import test_divisor as divisor
import test_runner as runner


def solve():
    n = 1000
    maximum = 0
    answer = 0
    for i in range(3, n, 2):
        if i % 5 == 0:
            continue
        r = 10
        length = 1
        while r % i != 1:
            r = r * 10
            length = length + 1
        if maximum < length:
            maximum = length
            answer = i
    return answer


def test():
    right_answer = 983
    runner.run(solve, right_answer)


if __name__ == '__main__':
    test()
