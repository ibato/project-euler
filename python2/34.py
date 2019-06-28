from time import *

# 1
start = time()
factorial = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
answer = 0
for i in range(10, 362880 * 6):
    n = str(i)
    if (n.count('1') + n.count('0')) % 2 != 0 and i % 2 == 0: continue
    if (n.count('1') + n.count('0')) % 2 == 0 and i % 2 != 0: continue
    if len(n) == 2:
        if '5' in n or '6' in n or '7' in n or '8' in n or '9' in n: continue
    elif len(n) == 3:
        if '7' in n or '8' in n or '9' in n: continue
    elif len(n) == 4:
        if '8' in n or '9' in n: continue
    elif len(n) == 5:
        if '9' in n: continue
    elif len(n) == 6:
        if '9' not in n: continue
    elif len(n) == 7:
        if n.count('9') < 3 or n.count('9') > 5: continue
    s = reduce(lambda x, y: x + y, [factorial[int(n[j])] for j in range(len(n))])
    if i == s:
        answer = answer + i
end = time()
print answer, end - start

# 2
start = time()
factorial = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
answer = 0
for i in range(10, 362880 * 6):
    n = str(i)
    s = reduce(lambda x, y: x + y, [factorial[int(n[j])] for j in range(len(n))])
    if i == s:
        answer = answer + i
end = time()
print answer, end - start
