from time import time
from math import sqrt
import test_palindrome as pdr

# 004.Largest palindrome product
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


def test():
    right_answer = 906609

    start = time()
    answer = first_approach()
    assert answer == right_answer
    print("Answer:", answer)
    end = time()
    print("Execution time:", end - start)

    start = end
    answer = second_approach()
    assert answer == right_answer
    print("Answer:", answer)
    end = time()
    print("Execution time:", end - start)


if __name__ == '__main__':
    test()
