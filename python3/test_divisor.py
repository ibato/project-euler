from time import time
from math import sqrt


def get_num_of_divisors(n):
    count = 0
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            count = count + 1
    if int(sqrt(n)) * int(sqrt(n)) == n:
        return count * 2 - 1
    return count * 2


def get_sum_of_proper_divisors(n):
    if n == 1 or n == 2:
        return n - 1
    summation = 0
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            summation = summation + i + n / i
    if int(sqrt(n)) == sqrt(n):
        return int(summation - sqrt(n) - n)
    return int(summation - n)


def test():
    assert get_num_of_divisors(5) == 2
    assert get_sum_of_proper_divisors(10) == 8


if __name__ == '__main__':
    start = time()
    test()
    print("Execution time:", time() - start)
