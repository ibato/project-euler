from time import *
from math import *

start = time()
n = 64000000
summation = 7966336
for i in range(931000, n):
    if i % 1000 == 0: print i, summation
    current = reduce(lambda x, y: x + y * y, filter(lambda x: i % x == 0, range(1, i + 1)))
    if int(sqrt(current)) == sqrt(current):
        summation = summation + i
end = time()
print summation, end - start

# 931000 7966336
