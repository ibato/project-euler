from time import time
import test_pandigital as pandigital
import test_runner as runner


def solve():
    for i in range(9999, 2, -1):
        answer = ""
        for j in range(1, 10):
            answer = answer + str(i * j)
            if len(answer) >= 9:
                break
        if pandigital.is_pandigital(answer, 123456789):
            break
    return int(answer)


def test():
    right_answer = 932718654
    runner.run(solve, right_answer)


if __name__ == '__main__':
    test()
