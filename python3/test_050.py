from time import time
from functools import reduce
import test_prime as prm
import test_runner as runner


def solve():
    answer = 0
    num = 1000000

    primes = prm.find_primes(1, num)
    summation = 0
    count = 0
    for i in range(len(primes)):
        summation = summation + primes[i]
        count = count + 1
        if (summation + primes[i + 1] >= num):
            break

    for i in range(count, 1, -1):
        for j in range(num - i):
            s = reduce(lambda x, y: x + y, primes[j:j + i])
            if s > num:
                break
            if prm.is_prime(s):
                answer = s
                break
        if answer != 0:
            break
    return answer


def test():
    right_answer = 997651
    runner.run(solve, right_answer)


if __name__ == '__main__':
    test()
