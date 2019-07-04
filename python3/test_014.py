from time import time
from functools import reduce
import test_runner as runner

# 014. Longest Collatz sequence
# https://projecteuler.net/problem=14


given = 1000000
d = [0] * (given + 1)


def get_length_of_chain(n):
    n = int(n)
    if n < given and d[n] != 0:
        return d[n]
    if n == 1:
        return 1
    if n % 2 == 0:
        l = get_length_of_chain(n / 2)
        if n / 2 < given:
            d[int(n / 2)] = l
    else:
        l = get_length_of_chain(3 * n + 1)
        if 3 * n + 1 < given:
            d[3 * n + 1] = l
    return l + 1


def solve():
    answer = 0
    max_length = 0
    for i in range(1, given + 1):
        d[i] = get_length_of_chain(i)
        if max_length < d[i]:
            max_length = d[i]
            answer = i
    return answer


def test():
    right_answer = 837799
    runner.run(solve, right_answer)


if __name__ == '__main__':
    test()
