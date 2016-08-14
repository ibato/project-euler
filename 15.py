from time import *
from combinatorics import *

# 1
start = time()
answer =  nCr_v1(40, 20)
end = time()
print answer, end - start

# 2
start = time()
answer =  nCr_v2(40, 20)
end = time()
print answer, end - start

# 3
start = time()
answer =  nCr_v3(40, 20)
end = time()
print answer, end - start
