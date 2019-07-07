from time import time
import test_runner as runner


def solve():
    answer = 1
    index = 0
    for i in range(1, 1000000):
        index = index + len(str(i))
        if index > 10 and index < 10 + len(str(i)):
            answer = answer * int(str(i)[len(str(i)) - (index - 10) - 1])
        elif index > 100 and index < 100 + len(str(i)):
            answer = answer * int(str(i)[len(str(i)) - (index - 100) - 1])
        elif index > 1000 and index < 1000 + len(str(i)):
            answer = answer * int(str(i)[len(str(i)) - (index - 1000) - 1])
        elif index > 10000 and index < 10000 + len(str(i)):
            answer = answer * int(str(i)[len(str(i)) - (index - 10000) - 1])
        elif index > 100000 and index < 100000 + len(str(i)):
            answer = answer * int(str(i)[len(str(i)) - (index - 100000) - 1])
        elif index > 1000000 and index < 1000000 + len(str(i)):
            answer = answer * int(str(i)[len(str(i)) - (index - 1000000) - 1])
    return answer


def test():
    right_answer = 210
    runner.run(solve, right_answer)


if __name__ == '__main__':
    test()
