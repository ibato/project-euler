from time import time
import test_runner as runner


def solve():
    return len(set(a ** b for a in range(2, 101) for b in range(2, 101)))


def test():
    right_answer = 9183
    runner.run(solve, right_answer)


if __name__ == '__main__':
    test()
