from time import time
import test_palindrome as pal
import test_runner as runner


def solve():
    return sum([1 for i in range(1, 10000) if is_lychrel(i)])


def is_lychrel(num):
    for i in range(50):
        num = num + int(str(num)[::-1])
        if pal.is_palindrome(num):
            return False
    return True


def test():
    right_answer = 249
    runner.run(solve, right_answer)


if __name__ == '__main__':
    test()
