from time import *

# 1
start = time()
n = 100
g = []
for a in range(2, n + 1):
    for b in range(2, n + 1):
        if (a ** b) not in g:
            g.append(a ** b)
end = time()
print len(g), end - start

# 2
start = time()
answer = len(set(a ** b for a in range(2, 101) for b in range(2, 101)))
end = time()
print answer, end - start
