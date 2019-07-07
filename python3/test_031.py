from time import time
import test_runner as runner


def solve():
    dp = []
    for i in range(8):
        dp.append([0] * 201)
    coin = [1, 2, 5, 10, 20, 50, 100, 200]
    for i in range(1, 201):
        dp[0][i] = 1
    for i in range(1, 8):
        for j in range(1, 201):
            if j % coin[i] == 0:
                dp[i][j] = 1
            for k in range(0, j, coin[i]):
                dp[i][j] = dp[i][j] + dp[i - 1][j - k]
    return dp[7][200]


def test():
    right_answer = 73682
    runner.run(solve, right_answer)


if __name__ == '__main__':
    test()
