from time import time
from sys import maxsize
import test_polygonal as polygonal
import test_runner as runner


def solve():
    answer = maxsize
    n = 1
    while True:
        n = n + 1
        for k in range(1, int(n / 2 + 1)):
            smaller = (k * (3 * k - 1)) / 2
            bigger = ((n - k) * (3 * (n - k) - 1)) / 2
            if polygonal.is_pentagonal(bigger + smaller) and polygonal.is_pentagonal(bigger - smaller):
                answer = bigger - smaller
                break
        if answer != maxsize:
            break
    return answer


def test():
    right_answer = 5482660
    runner.run(solve, right_answer)


if __name__ == '__main__':
    test()
