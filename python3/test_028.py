from time import time
import test_runner as runner


def solve():
    answer = [1, ]
    count = 4
    diff = 2
    i = 2

    while True:
        if answer[-1] + diff == i:
            answer.append(i)
            count = count - 1
        if count == 0:
            diff = diff + 2
            count = 4
        if diff > 1000:
            return sum(answer)
        i = i + 1

    return -1


def test():
    right_answer = 669171001
    runner.run(solve, right_answer)


if __name__ == '__main__':
    test()
