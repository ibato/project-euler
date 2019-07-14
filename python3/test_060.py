from time import time
from itertools import combinations
import test_prime as prm
import test_runner as runner


cache = []


def solve():
    primes = prm.find_primes(2, 10000)
    primes.remove(2)
    primes.remove(5)

    candidates = []
    answer = 50000
    start = time()

    for cb5 in combinations(primes, 2):
        current = time()
        if (current - start) % 10 >= 0 and (current - start) % 10 < 0.001:
            print("log: %s, %s"% (format_time(current - start), cb5))
        for cb2 in combinations(cb5, 2):
            if cb2 not in cache:
                if not can_produce_prime(cb2[0], cb2[1]):
                    break
        else:
            candidates.append(cb5)
    
    n_plus_1 = candidates
    for n in range(3):
        n_plus_1 = find_n_plus_1_answers(n_plus_1)
        print(n_plus_1)
    print(n_plus_1)

    return sorted(map(lambda x: sum(x), n_plus_1))[0]


def format_time(seconds):
    if seconds < 60:
        return str(int(seconds)) + " secs"
    elif seconds < 3600:
        return str(int(seconds / 60)) + " mins " + str(int((seconds % 60))) + " secs"
    return str(int(seconds / 3600)) + " hours " + str(int((seconds % 3600) / 60)) + " mins"


def find_n_plus_1_answers(candidates):
    print("candidates[0]: ", candidates[0])
    start = time()
    n_plus_1 = []
    for candidate in candidates:
        primes = prm.find_primes(candidate[-1], 10000)
        for p in primes:
            current = time()
            if (current - start) % 10 >= 0 and (current - start) % 10 < 0.001:
                print("log: %s, %s, %d"% (format_time(current - start), candidate, p))
            for cd in candidate:
                if (cd, p) not in cache:
                    if not can_produce_prime(cd, p):
                        break
            else:
                n_plus_1.append((cd, p))
    return n_plus_1


def can_produce_prime(n1, n2):
    a1 = int(str(n1) + str(n2))
    a2 = int(str(n1) + str(n2))
    if prm.is_prime(a1) and prm.is_prime(a2):
        cache.append((n1, n2))
        return True
    return False

def test():
    right_answer = 26033
    runner.run(solve, right_answer)


if __name__ == '__main__':
    test()
