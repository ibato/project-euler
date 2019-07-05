from time import time
import test_runner as runner


def solve():
    answer = 0
    for i in range(2, 354294):
        sumofpowers = 0
        for j in str(i):
            sumofpowers = sumofpowers + (int(j) ** 5)
        if sumofpowers == i:
            answer = answer + i
    return answer


def test():
    right_answer = 443839
    runner.run(solve, right_answer)


if __name__ == '__main__':
    test()
