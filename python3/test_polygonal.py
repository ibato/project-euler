from time import time
from math import *


def is_triangle(num):
    d = (-1 + sqrt(8 * num + 1)) / 2
    if floor(d) == d:
        return True
    return False


def is_pentagonal(num):
    d = (1 + (sqrt(24 * num + 1))) / 6
    if floor(d) == d:
        return True
    return False


def is_hexagonal(num):
    d = (1 + sqrt(8 * num + 1)) / 4
    if floor(d) == d:
        return True
    return False


def is_heptagonal(num):
    d = (3 + sqrt(40 * num + 9)) / 10
    if floor(d) == d:
        return True
    return False


def is_octagonal(num):
    d = (1 + sqrt(3 * num + 1)) / 3
    if floor(d) == d:
        return True
    return False


def find_triangles(start, end):
    return [i for i in range(start, end) if is_triangle(i)]


def find_squares(start, end):
    return [i for i in range(start, end) if sqrt(i) == floor(sqrt(i))]


def find_pentagonals(start, end):
    return [i for i in range(start, end) if is_pentagonal(i)]


def find_hexagonals(start, end):
    return [i for i in range(start, end) if is_hexagonal(i)]


def find_heptagonals(start, end):
    return [i for i in range(start, end) if is_heptagonal(i)]


def find_octagonals(start, end):
    return [i for i in range(start, end) if is_octagonal(i)]


def test():
    assert is_pentagonal(92) == True
    assert is_pentagonal(48) == False


if __name__ == '__main__':
    start = time()
    test()
    print("Execution time:", time() - start)
