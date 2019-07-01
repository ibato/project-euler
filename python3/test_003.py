from time import time
from math import sqrt
import test_prime as prime

# 003. Largest prime factor
# https://projecteuler.net/problem=3


# First Approach - Test all numbers
#
# This approach tests all numbers whether that is the prime factor or not and acquire the largest of them.
def first_approach():
    num = 600851475143
    answer = 0
    for i in range(int(sqrt(num)), 2, -1):
        if prime.is_prime(i) == True and num % i == 0:
            answer = i
            break
    return answer


# Second Approach - Test the numbers ended with 1, 3, 7, 9 only
#
# All factors are ended with 1, 3, 7 and 9 since the number 600851475143 isn't divided by 2 and 5.
# Even multiples of 2 and 5 are not prime except for 2.
#
# There is no significant difference in execution time compared to the first approach.
def second_approach():
    num = 600851475143
    answer = 0
    for i in range(int(sqrt(num)), 2, -1):
        if i % 2 == 0 or i % 5 == 0:
            continue
        if prime.is_prime(i) == True and num % i == 0:
            answer = i
            break
    return answer


# Third Approach - Make the number to get smaller by dividing it
#
# My is_prime() method is O(sqrt{n}),
# so this is much faster to divide the numbers directly and make it smaller and smaller.
def third_approach():
    num = 600851475143
    answer = 0
    for i in range(3, int(sqrt(num)), 2):
        if num % i == 0:
            answer = i
            n = n / i
            i = i - 2
    return answer


def test():
    right_answer = 6857

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

    start = end
    answer = third_approach()
    assert answer == right_answer
    print("Answer:", answer)
    print("Execution time:", time() - start)


if __name__ == '__main__':
    test()
