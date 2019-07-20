from time import time
from itertools import combinations
import test_prime as prm
import test_runner as runner


cache = []
start = time()

primes_sieve = prm.find_primes(2, 100000000)
primes = prm.find_primes(2, 10000)

def solve():
    primes.remove(2)
    primes.remove(5)

    for a in range(len(primes)):
        for b in range(a + 1, len(primes)):
            if not can_produce_prime(primes[a], primes[b]):
                continue

            for c in range(b + 1, len(primes)):
                if not can_produce_prime(primes[a], primes[c]) or not can_produce_prime(primes[b], primes[c]):
                    continue

                for d in range(c + 1, len(primes)):
                    if not can_produce_prime(primes[a], primes[d]) or not can_produce_prime(primes[b], primes[d]) or not can_produce_prime(primes[c], primes[d]):
                        continue

                    for e in range(d + 1, len(primes)):
                        n1 = primes[a]; n2 = primes[b]; n3 = primes[c]; n4 = primes[d]; n5 = primes[e]
                        if can_produce_prime(n1, n5) and can_produce_prime(n2, n5) and can_produce_prime(n3, n5) and can_produce_prime(n4, n5):
                            print("answer: ", sum((n1, n2, n3, n4, n5)), (n1, n2, n3, n4, n5))
                            return sum((n1, n2, n3, n4, n5))
                        else:
                            continue


def format_time(seconds):
    if seconds < 60:
        return str(int(seconds)) + " secs"
    elif seconds < 3600:
        return str(int(seconds / 60)) + " mins " + str(int((seconds % 60))) + " secs"
    return str(int(seconds / 3600)) + " hours " + str(int((seconds % 3600) / 60)) + " mins"


def can_produce_prime(n1, n2):
    current = time()
    if (current - start) % 10 >= 0 and (current - start) % 10 < 0.1:
        print("log: %s, %s" % (format_time(current - start), (n1, n2)))

    if (n1, n2) in cache:
        return True

    a1 = int(str(n1) + str(n2))
    a2 = int(str(n2) + str(n1))

    if a1 in primes_sieve and a2 in primes_sieve:
        if n1 > 1000 and n2 > 1000:
            print(a1, a2, n1, n2)
        cache.append((n1, n2))
        return True
    return False

def test():
    right_answer = 26033
    runner.run(solve, right_answer)


if __name__ == '__main__':
    test()
