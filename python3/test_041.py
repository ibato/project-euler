from time import time
from itertools import permutations
import test_prime as prime
import test_runner as runner


def solve():
    p = permutations(['7', '6', '5', '4', '3', '2', '1'])
    for each in p:
        joined = "".join(each)
        if prime.is_prime(int(joined)) == True:
            answer = joined
            break
    return int(answer)


def test():
    right_answer = 7652413
    runner.run(solve, right_answer)


if __name__ == '__main__':
    test()
