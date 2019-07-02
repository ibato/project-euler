from time import time


def is_palindrome(s):
    if not isinstance(s, str):
        s = str(s)
    return s == s[::-1]


def test():
    assert is_palindrome(1234567890987654321) == True
    assert is_palindrome(4) == True


if __name__ == '__main__':
    start = time()
    test()
    print("Execution time:", time() - start)
