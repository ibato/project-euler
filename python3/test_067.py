from time import time
import test_matrix as matrix
import test_file as file
import test_runner as runner


def solve():
    p = []
    f = file.open_file('./test_067_triangle.txt')
    for line in f:
        p.append(line.strip().split(' '))

    dp = matrix.get_empty_matrix(len(p))
    dp[0][0] = int(p[0][0])
    for i in range(1, len(p)):
        for j in range(len(p[i])):
            dp[i][j] = max(dp[i - 1][j - 1] + int(p[i][j]),
                           dp[i - 1][j] + int(p[i][j]))
    end = time()
    return max(dp[len(p) - 1])


def test():
    right_answer = 7273
    runner.run(solve, right_answer)


if __name__ == '__main__':
    test()
