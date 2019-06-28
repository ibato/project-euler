from time import *

def getEmptyMatrix(num):
    result = []
    for i in range(num):
        t = [0] * num
        result.append(t)
    return result

start = time()
p = []
f = open('triangle.txt', 'r')
for line in f:
    p.append(line.strip().split(' '))
print p

dp = getEmptyMatrix(len(p))
dp[0][0] = int(p[0][0])
for i in range(1, len(p)):
    for j in range(len(p[i])):
        dp[i][j] = max(dp[i - 1][j - 1] + int(p[i][j]), dp[i - 1][j] + int(p[i][j]))
end = time()
print max(dp[len(p) - 1]), end - start
