from time import time
from functools import reduce
import test_pandigital as pandigital
import test_runner as runner


def solve():
    factorial = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
    answer = 0
    for i in range(10, 362880 * 6):
        n = str(i)
        s = reduce(lambda x, y: x + y, [factorial[int(n[j])]
                                        for j in range(len(n))])
        if i == s:
            answer = answer + i
    return answer


def test():
    right_answer = 40730
    runner.run(solve, right_answer)


if __name__ == '__main__':
    test()
