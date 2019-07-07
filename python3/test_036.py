from time import time
import test_palindrome as palindrome
import test_runner as runner


def solve():
    answer = 0
    for i in range(1, 1000000, 2):
        decimal = str(i)
        binary = str(bin(i))[2::]
        if palindrome.is_palindrome(decimal) and palindrome.is_palindrome(binary):
            answer = answer + i
    return answer


def test():
    right_answer = 872187
    runner.run(solve, right_answer)


if __name__ == '__main__':
    test()
