from combinatorics import *
from time import *

def getEmptyMatrix(row, col, val):
    returnMatrix = []
    for r in range(row):
        aRow = []
        for c in range(col):
            aRow.append(val)
        returnMatrix.append(aRow)
    return returnMatrix

# dp
start = time()
increasing = getEmptyMatrix(101, 10, 0)
for i in range(1, len(increasing[1])):
    increasing[1][i] = 1
for i in range(2, len(increasing)):
    for j in range(1, len(increasing[i])):
        for k in range(j, len(increasing[i - 1])):
            increasing[i][j] = increasing[i][j] + increasing[i - 1][k]

increasingSum = 0
for i in range(1, len(increasing)):
    for j in range(1, len(increasing[i])):
        increasingSum = increasingSum + increasing[i][j]
print "increasingSum:", increasingSum

decreasing = getEmptyMatrix(101, 10, 0)
for i in range(len(decreasing[1])):
    decreasing[1][i] = 1
for i in range(2, len(decreasing)):
    for j in range(len(decreasing[i])):
        for k in range(j + 1):
            decreasing[i][j] = decreasing[i][j] + decreasing[i - 1][k]

decreasingSum = 0
for i in range(1, len(decreasing)):
    for j in range(1, len(decreasing[i])):
        decreasingSum = decreasingSum + decreasing[i][j]
print "decreasingSum:", decreasingSum
end = time()

print "dp solution:", increasingSum + decreasingSum - 900, end - start, "\n"

# combinatorics
start = time()
increasingSum = nCr(109, 9) - 1
decreasingSum = nCr(110, 10) - 1
print "increasingSum:", increasingSum
print "decreasingSum:", decreasingSum
end = time()
print "combinatorics solution:", increasingSum + decreasingSum - 1000, end - start
