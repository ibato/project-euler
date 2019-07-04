from time import time
from math import factorial


def nCr(n, r):
    f = factorial
    return f(n) / (f(r) * f(n-r))


def test():
    assert nCr(3, 2) == 3
    assert nCr(5, 2) == 10


if __name__ == '__main__':
    start = time()
    test()
    print("Execution time:", time() - start)
