from math import *

def is_palindrome(s):
    if not isinstance(s, str):
        s = str(s)
    return s == s[::-1]

def is_pandigital(s, c):
    if not isinstance(s, str):
        s = str(s)
    return "".join(sorted(s)) == c

def is_triangle(num):
    d = (-1 + sqrt(8 * num + 1)) / 2
    if floor(d) == d:
        return True;
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

def acquire_empty_matrix(n):
    result = []
    for i in range(n):
        t = [0] * n
        result.append(t)
    return result

def acquire_triangle(start, end):
    return [i for i in range(start, end) if is_triangle(i)]

def acquire_square(start, end):
    return [i for i in range(start, end) if sqrt(i) == floor(sqrt(i))]

def acquire_pentagonal(start, end):
    return [i for i in range(start, end) if is_pentagonal(i)]

def acquire_hexagonal(start, end):
    return [i for i in range(start, end) if is_hexagonal(i)]

def acquire_heptagonal(start, end):
    return [i for i in range(start, end) if is_heptagonal(i)]

def acquire_octagonal(start, end):
    return [i for i in range(start, end) if is_octagonal(i)]
