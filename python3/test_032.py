from time import time
from functools import reduce
import test_pandigital as pandigital
import test_runner as runner


def solve():
    answer = []
    for multiplicand in range(1, 10000):
        for multiplier in range(1, int(10000 / multiplicand)):
            if pandigital.is_pandigital(str(multiplicand) + str(multiplier) + str(multiplicand * multiplier), 123456789):
                answer.append(multiplicand * multiplier)
    return reduce(lambda x, y: x + y, set(answer))


def test():
    right_answer = 45228
    runner.run(solve, right_answer)


if __name__ == '__main__':
    test()
