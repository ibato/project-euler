from time import time
import test_divisor as divisor
import test_runner as runner

# https://projecteuler.net/problem=23


def solve():
    n = 28123
    abundant = list(filter(lambda i: divisor.get_sum_of_proper_divisors(i)
                           > i, range(12, n + 1)))
    sieve = [False] * (n + 1)
    for i in range(len(abundant)):
        for j in range(i, len(abundant)):
            if abundant[i] + abundant[j] <= n:
                sieve[abundant[i] + abundant[j]] = True
            else:
                break
    return sum(filter(lambda x: sieve[x] == False, range(1, n + 1)))


def test():
    right_answer = 4179871
    runner.run(solve, right_answer)


if __name__ == '__main__':
    test()
