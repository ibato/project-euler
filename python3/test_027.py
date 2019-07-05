from time import time
import test_prime as prime
import test_runner as runner


def solve():
    c = 1000
    maximum = 0
    answer = 0
    pr = prime.find_primes(1, c)
    for a in range(-c + 1, c):
        for b in pr:
            n = 1
            while True:
                if n * n + a * n + b <= 0:
                    break
                if prime.is_prime(n * n + a * n + b) == False:
                    break
                n = n + 1
            if maximum < n:
                maximum = n
                answer = a * b
    return answer


def test():
    right_answer = -59231
    runner.run(solve, right_answer)


if __name__ == '__main__':
    test()
