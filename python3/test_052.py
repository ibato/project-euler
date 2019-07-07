from time import time
from functools import reduce
import test_prime as prm
import test_runner as runner


def solve():
    answer = 0
    i = 0
    while True:
        i = i + 1
        if is_answer(i):
            answer = i
            break
    return answer


def is_answer(num):
    l = [x for x in str(num)]
    for i in range(1, 6):
        if sorted(l) != sorted([x for x in str(num * i)]):
            return False
    return True


def test():
    right_answer = 142857
    runner.run(solve, right_answer)


if __name__ == '__main__':
    test()
