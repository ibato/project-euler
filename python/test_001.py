from time import time


def solve():
    return sum(filter(lambda x: x % 3 == 0 or x % 5 == 0, range(1, 1000)))


def test():
    answer = solve()
    print("Answer:", answer)
    assert answer == 233168


if __name__ == '__main__':
    start = time()
    test()
    print("Execution time:", time() - start)
