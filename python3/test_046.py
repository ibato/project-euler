from time import time
from math import sqrt
import test_prime as prime
import test_runner as runner


def solve():
    answer = 0
    n = 3
    while True:
        if prime.is_prime(n) == False and is_not_satisfy_conjecture(n):
            answer = n
            break
        n = n + 2
        if n % 5 == 0:
            n = n + 2
    return answer


def is_not_satisfy_conjecture(n):
    for i in range(n):
        if prime.is_prime(i) == True:
            j = sqrt((n - i) / 2)
            if j == int(j):
                return False
    return True


def test():
    right_answer = 5777
    runner.run(solve, right_answer)


if __name__ == '__main__':
    test()
