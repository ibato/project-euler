from time import *

# 1
start = time()
answer = max([sum([int(x) for x in str(a ** b)]) for a in range(1, 100) for b in range(1, 100)])
end = time()
print answer, end - start
