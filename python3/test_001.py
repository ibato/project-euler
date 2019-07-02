from time import time
import test_runner as runner

# 001. Multiples of 3 and 5
# https://projecteuler.net/problem=1


# This is just the brute force attack.
def solve():
    return sum(filter(lambda x: x % 3 == 0 or x % 5 == 0, range(1, 1000)))


def test():
    right_answer = 233168
    runner.run(solve, right_answer)


if __name__ == '__main__':
    start = time()
    test()
    print("Execution time:", time() - start)
