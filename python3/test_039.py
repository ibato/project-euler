from time import time
import test_runner as runner


def solve():
    answer = 0
    maximum = 0
    for p in range(1000, 12, -1):
        n = get_num_of_solution(p)
        if maximum < n:
            maximum = n
            answer = p
    return answer


def get_num_of_solution(p):
    count = 0
    for z in range(int(p / 2), int(p / 3), -1):
        for x in range(1, int(z / 2)):
            y = p - x - z
            if z * z == x * x + y * y:
                count = count + 1
    return count


def test():
    right_answer = 840
    runner.run(solve, right_answer)


if __name__ == '__main__':
    test()
