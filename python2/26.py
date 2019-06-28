from time import *

# 1
start = time()
n = 1000
maximum = 0
answer = 0
for i in range(2, n):
    d = []
    d.append(1)
    while True:
        r = (d[len(d) - 1] * 10) % i
        if r == 0: break
        if r in d:
            if maximum < len(d) - d.index(r):
                maximum = len(d) - d.index(r)
                answer = i
            break
        else:
            d.append(r)
end = time()
print answer, end - start

# 2
start = time()
n = 1000
maximum = 0
answer = 0
for i in range(3, n, 2):
    if i % 5 == 0: continue
    d = []
    d.append(1)
    while True:
        r = (d[len(d) - 1] * 10) % i
        if r == 0: break
        if r in d:
            if maximum < len(d) - d.index(r):
                maximum = len(d) - d.index(r)
                answer = i
            break
        else:
            d.append(r)
end = time()
print answer, end - start

# 3
start = time()
n = 1000
maximum = 0
answer = 0
for i in range(3, n, 2):
    if i % 5 == 0: continue
    r = 10
    length = 1
    while r % i != 1:
        r = r * 10
        length = length + 1
    if maximum < length:
        maximum = length
        answer = i
end = time()
print answer, end - start
