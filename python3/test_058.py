from time import time
import test_prime as prm
import test_runner as runner


def solve():
    num_of_primes = 3
    current_prime = 9
    n = 2
    while float(num_of_primes) / float(4 * n - 3) >= 0.1:
        n = n + 1
        for i in range(4):
            if prm.is_prime(current_prime):
                num_of_primes = num_of_primes + 1
            current_prime = current_prime + 2 * (n - 1)
    return 2 * n - 1


def test():
    right_answer = 26241
    runner.run(solve, right_answer)


if __name__ == '__main__':
    test()
