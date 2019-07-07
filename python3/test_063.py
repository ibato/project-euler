from time import time
import test_runner as runner


def solve():
    answer = 0
    for n in range(1, 22):
        for i in range(1, 10):  # 10^n is (n+1) digits
            if (len(str(i ** n)) == n):
                answer = answer + 1
    return answer


def test():
    right_answer = 49
    runner.run(solve, right_answer)


if __name__ == '__main__':
    test()
