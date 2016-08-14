from time import *
from combinatorics import *

start = time()
count = 0
for n in range(1, 101):
    for r in range(0, n + 1):
        if nCr_v2(n, r) > 1000000:
            count = count + 1
end = time()
print count, end - start

start = time()
print len([(n, r) for n in range(1, 101) for r in range(0, n + 1) if nCr_v2(n, r) > 1000000]), time() - start
