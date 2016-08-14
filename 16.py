from math import *
from time import *
from combinatorics import *

# 1
start = time()
length = 302
power = 1000
n = [0] * length
n[length - 1] = 1
for i in range(1, power + 1):
    carry = 0
    answer = 0
    for j in range(length - 1, -1, -1):
        n[j] = n[j] * 2 + carry
        if n[j] >= 10:
            n[j] = n[j] - 10
            carry = 1
        else:
            carry = 0
        answer = answer + n[j]
end = time()
print answer, end - start

# 2 - nCr_v1
start = time()
n = 0
for i in range(500):
    n = n + nCr_v1(1000, i)
n = n * 2 + nCr_v1(1000, 500)
answer = 0
for i in range(len(str(n))):
    answer = answer + int(str(n)[i])
end = time()
print answer, end - start

# 3 - nCr_v2
start = time()
n = 0
for i in range(500):
    n = n + nCr_v2(1000, i)
n = n * 2 + nCr_v2(1000, 500)
answer = 0
for i in range(len(str(n))):
    answer = answer + int(str(n)[i])
end = time()
print answer, end - start

# 4 - nCr_v13
start = time()
n = 0
for i in range(500):
    n = n + nCr_v3(1000, i)
n = n * 2 + nCr_v3(1000, 500)
answer = 0
for i in range(len(str(n))):
    answer = answer + int(str(n)[i])
end = time()
print answer, end - start

# 5 - ?
start = time()
answer = reduce(int.__add__, map(int, str(2 ** 1000)))
end = time()
print answer, end - start
