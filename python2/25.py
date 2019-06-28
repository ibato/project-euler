from time import *
from math import *

# 1
start = time()
a = 1
b = 1
answer = 2
while True:
    c = a + b
    answer = answer + 1
    if len(str(c)) == 1000:
        break
    a = b
    b = c
end = time()
print answer, end - start

# 2
start = time()
f = [1, 1]
while len(str(f[len(f) - 1])) < 1000:
    f.append(f[len(f) - 2] + f[len(f) - 1])
end = time()
print len(f), end - start
