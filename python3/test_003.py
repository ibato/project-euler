from time import time
from math import sqrt
from test_prime import is_prime

# 003. Largest prime factor
# https://projecteuler.net/problem=3


# First Approach - Test all numbers
#
# This approach tests all numbers whether that is the prime factor or not
# and acquire the largest of them.
def first_approach():
    n = 600851475143
    answer = 0
    for i in range(int(sqrt(n)), 2, -1):
        if is_prime(i) == True and n % i == 0:
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
    n = 600851475143
    answer = 0
    for i in range(int(sqrt(n)), 2, -1):
        if i % 2 == 0 or i % 5 == 0:
            continue
        if is_prime(i) == True and n % i == 0:
            answer = i
            break
    return answer


# Third Approach - Make the number to get smaller by dividing it
#
# My is_prime() method is O(sqrt{n}),
# so this is much faster to divide the numbers directly and make it smaller and smaller.
def third_approach():
    n = 600851475143
    answer = 0
    for i in range(3, int(sqrt(n)), 2):
        if n % i == 0:
            answer = i
            n = n / i
            i = i - 2
    return answer


def test():
    right_answer = 6857

    answer = first_approach()
    print("Answer:", answer)
    assert answer == right_answer

    answer = second_approach()
    print("Answer:", answer)
    assert answer == right_answer


if __name__ == '__main__':
    start = time()
    test()
    print("Execution time:", time() - start)
