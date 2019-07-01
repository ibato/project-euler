from time import time
from math import sqrt
from prime import is_prime


def solve():
    n = 600851475143
    answer = 0
    for i in range(int(sqrt(n)), 2, -1):
        if is_prime(i) == True and n % i == 0:
            answer = i
            break
    return answer


def test():
    answer = solve()
    print("Answer:", answer)
    assert answer == 6857


if __name__ == '__main__':
    start = time()
    test()
    print("Execution time:", time() - start)
