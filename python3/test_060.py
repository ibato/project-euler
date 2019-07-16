from time import time
from itertools import combinations
import test_prime as prm
import test_runner as runner


cache = []
primes_100000 = prm.find_primes(2, 100000)
primes = prm.find_primes(2, 10000)

def solve():
    primes.remove(2)
    primes.remove(5)

    start = time()

    for a in range(len(primes)):
        for b in range(a + 1, len(primes)):
            for c in range(b + 1, len(primes)):
                for d in range(c + 1, len(primes)):
                    for e in range(d + 1, len(primes)):
                        n1 = primes[a]; n2 = primes[b]; n3 = primes[c]; n4 = primes[d]; n5 = primes[e]

                        current = time()
                        if (current - start) % 10 >= 0 and (current - start) % 10 < 0.001:
                            print("log: %s, %s" % (format_time(current - start), (n1, n2, n3, n4, n5)))

                        for cb in combinations((n1, n2, n3, n4, n5), 2):
                            if cb not in cache:
                                if not can_produce_prime(cb[0], cb[1]):
                                    break
                        else:
                            return sum((n1, n2, n3, n4, n5))


def format_time(seconds):
    if seconds < 60:
        return str(int(seconds)) + " secs"
    elif seconds < 3600:
        return str(int(seconds / 60)) + " mins " + str(int((seconds % 60))) + " secs"
    return str(int(seconds / 3600)) + " hours " + str(int((seconds % 3600) / 60)) + " mins"


def can_produce_prime(n1, n2):
    a1 = int(str(n1) + str(n2))
    a2 = int(str(n1) + str(n2))

    if a1 in primes_100000 and a2 in primes_100000:
        cache.append((n1, n2))
        return True
    return False

def test():
    right_answer = 26033
    runner.run(solve, right_answer)


if __name__ == '__main__':
    test()
