from time import time
from math import sqrt
from functools import reduce
import os
import test_file as file
import test_runner as runner


def solve():
    f = file.open_file("./test_042_words.txt")
    words = f.read().replace("\"", "").split(",")
    return len(list(filter(lambda v: sqrt(1 + 8 * v) == int(sqrt(1 + 8 * v)), [reduce(lambda x, y: x + y, [ord(w[i]) - ord('A') + 1 for i in range(len(w))]) for w in words])))


def test():
    right_answer = 162
    runner.run(solve, right_answer)


if __name__ == '__main__':
    test()
