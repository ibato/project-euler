from time import time
import test_prime as prime

# 007. 10001st prime
# https://projecteuler.net/problem=7


# First Approach - Test all numbers
def first_approach():
    count = 0
    num = 1
    while True:
        num = num + 1
        if prime.is_prime(num) == True:
            count = count + 1
            if count == 10001:
                break
    return num


# Second Approach - Test the numbers ended with 1, 3, 7, 9 only
def second_approach():
    count = 1
    num = 1
    while True:
        num = num + 2
        if num % 5 == 0:
            continue
        if prime.is_prime(num) == True:
            count = count + 1
            if count == 10000:  # because we do not count 2
                break
    return num


def test():
    right_answer = 104743

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
