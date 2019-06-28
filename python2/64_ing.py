from time import *
from math import *

def acquire_a(i):
    return int(floor(i))

def acquire_r(i, a):
    return 1 / (i - a)

start = time()

n = 14
answer = 0

for i in range(2, n):
    if floor(sqrt(i)) == sqrt(i):
        continue
    t = sqrt(i)
    s = []
    while True:
        a = acquire_a(t)
        r = acquire_r(t, a)
        if len(s) > 0 and abs(s[0] - r) < 0.01:
            break
        s.append(r)
        t = r
    if len(s) % 2 == 1:
        answer = answer + 1
        print i, len(s)

end = time()

print answer, end - start
