from time import time
import test_combinatorics as cb
import test_runner as runner


def solve():
    return len([(n, r) for n in range(1, 101)
                for r in range(0, n + 1) if cb.nCr(n, r) > 1000000])


def test():
    right_answer = 4075
    runner.run(solve, right_answer)


if __name__ == '__main__':
    test()
