from time import time
import test_prime as prime
import test_runner as runner


def solve():
    n = 1000000
    primes = prime.find_primes(1, n)
    answer = 1
    for prm in primes:
        p = str(prm)
        if '0' in p or '2' in p or '4' in p or '6' in p or '8' in p:
            continue
        for i in range(len(p)):
            t = p[i:] + p[0:i]
            if prime.is_prime(int(t)) == False:
                break
        else:
            answer = answer + 1
    return answer


def test():
    right_answer = 55
    runner.run(solve, right_answer)


if __name__ == '__main__':
    test()
