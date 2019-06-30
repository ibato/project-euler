from time import time


def solve():
    a = 1
    b = 2
    summation = b
    while a + b < 4000000:
        c = a + b
        if c % 2 == 0:
            summation = summation + c
        a = b
        b = c
    return summation


def test():
    answer = solve()
    print("Answer:", answer)
    assert answer == 4613732


if __name__ == '__main__':
    start = time()
    test()
    print("Execution time:", time() - start)
