from time import time
from itertools import *
from functools import reduce
import test_prime as prime
import test_runner as runner


def solve():
    answer = 0
    primes = prime.find_primes(1000, 9999)
    for prm in primes:
        c = combinations(permutations([x for x in str(prm)]), 3)
        for each in c:
            first = int(reduce(lambda x, y: x + y, each[0]))
            second = int(reduce(lambda x, y: x + y, each[1]))
            third = int(reduce(lambda x, y: x + y, each[2]))
            if first > 1000 and second > first and third > second:
                if first + third == 2 * second and prime.is_prime(first) and prime.is_prime(second) and prime.is_prime(third):
                    if not first == 1487:
                        answer = str(first) + str(second) + str(third)
                        break
            if not answer == 0:
                break
    return int(answer)


def test():
    right_answer = 296962999629
    runner.run(solve, right_answer)


if __name__ == '__main__':
    test()
