from itertools import *
from time import *

start = time()
summation = 0
p = permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
for d in p:
    if d[3] % 2 != 0: continue
    if (d[2] + d[3] + d[4]) % 3 != 0: continue
    if d[5] != 5: continue
    if (100 * d[4] + 10 * d[5] + d[6]) % 7 != 0: continue
    if d[7] - d[6] != 6 and d[7] - d[6] != -5: continue
    if (100 * d[6] + 10 * d[7] + d[8]) % 13 != 0: continue
    if (100 * d[7] + 10 * d[8] + d[9]) % 17 != 0: continue
    summation = summation + reduce(lambda x, y: 10 * x + y, d)
end = time()
print summation, end - start
