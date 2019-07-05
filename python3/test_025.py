from time import time
import test_divisor as divisor
import test_runner as runner

# https://projecteuler.net/problem=23


def solve():
    f = [1, 1]
    while len(str(f[len(f) - 1])) < 1000:
        f.append(f[len(f) - 2] + f[len(f) - 1])
    return len(f)


def test():
    right_answer = 4782
    runner.run(solve, right_answer)


if __name__ == '__main__':
    test()
