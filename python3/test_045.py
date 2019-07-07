from time import time
import test_polygonal as polygonal
import test_runner as runner


def solve():
    answer = 0
    n = 144
    while True:
        h = n * (2 * n - 1)
        if polygonal.is_pentagonal(h) and polygonal.is_triangle(h):
            answer = h
            break
        n = n + 1
    return answer


def test():
    right_answer = 1533776805
    runner.run(solve, right_answer)


if __name__ == '__main__':
    test()
