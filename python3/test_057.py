from time import time
import test_runner as runner


def solve():
    answer = 0
    a = 2  # denominator
    b = 3  # numerator
    for i in range(999):
        c = a + b  # denominator
        d = 2 * a + b  # numerator
        a = c
        b = d
        if len(str(b)) > len(str(a)):
            answer = answer + 1
    return answer


def test():
    right_answer = 153
    runner.run(solve, right_answer)


if __name__ == '__main__':
    test()
