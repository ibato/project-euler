# 200h + 100g + 50f + 20e + 10d + 5c + 2b + a = 200

from time import *

start = time()
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
end = time()
print dp[7][200], end - start
