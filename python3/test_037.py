from time import time
import test_prime as prime
import test_runner as runner


def solve():
    answer = 0
    count = 0
    num = 7
    while count < 11:
        num = num + 2
        if '4' in str(num) or '6' in str(num) or '8' in str(num):
            continue
        if is_right_truncatable_primes(num) and is_left_truncatable_primes(num):
            answer = answer + num
            count = count + 1
    return answer


def is_right_truncatable_primes(p):
    if isinstance(p, str) == False:
        p = str(p)
    for i in range(len(p)):
        if prime.is_prime(int(p[i::])) == False:
            return False
    return True


def is_left_truncatable_primes(p):
    if isinstance(p, str) == False:
        p = str(p)
    for i in range(1, len(p)):
        if prime.is_prime(int(p[0: i])) == False:
            return False
    return True


def test():
    right_answer = 748317
    runner.run(solve, right_answer)


if __name__ == '__main__':
    test()
