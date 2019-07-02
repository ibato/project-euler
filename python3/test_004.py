from time import time
from math import sqrt
import test_palindrome as pdr
import test_runner as runner

# 004. Largest palindrome product
# https://projecteuler.net/problem=4


# First Approach - Test all numbers
#
# This approach tests all numbers whether that is the palindrome or not.
def first_approach():
    answer = 0
    for i in range(999, 100, -1):
        for j in range(999, 100, -1):
            if i != j:
                if pdr.is_palindrome(i * j) == True and answer < (i * j):
                    answer = i * j
    return answer


# Second Approach - Test the numbers which are able to divide into 11
#
# All palindrome numbers can be divided by 11
def second_approach():
    answer = 0
    for i in range(999, 100, -1):
        for j in range(999, 100, -1):
            if (i * j) % 11 == 0:
                if pdr.is_palindrome(i * j) == True and answer < (i * j):
                    answer = i * j
    return answer


# Third Approach - One-liner
#
# This is a one-liner solution. The logic is the same as the 2nd approach.
def third_approach():
    return max([i * j for i in range(999, 100, -1) for j in range(999, 100, -1)
                if (i * j) % 11 == 0 and pdr.is_palindrome(i * j) == True])


def test():
    right_answer = 906609

    runner.run(first_approach, right_answer)
    runner.run(second_approach, right_answer)
    runner.run(third_approach, right_answer)


if __name__ == '__main__':
    test()
