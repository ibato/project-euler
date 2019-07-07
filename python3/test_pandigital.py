from time import time


def is_pandigital(s, c):
    if not isinstance(s, str):
        s = str(s)
    return "".join(sorted(s)) == str(c)


def test():
    assert is_pandigital(15234, 12345) == True


if __name__ == '__main__':
    start = time()
    test()
    print("Execution time:", time() - start)
