from time import time
import test_runner as runner


def solve():
    return max([sum([int(x) for x in str(a ** b)]) for a in range(1, 100) for b in range(1, 100)])


def test():
    right_answer = 972
    runner.run(solve, right_answer)


if __name__ == '__main__':
    test()
