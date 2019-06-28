from time import *

# 3
given = 1000000
d = [0] * (given + 1)

def acquire_length_of_chain(n):
    if n < given and d[n] != 0:
        return d[n]
    if n == 1: return 1
    if n % 2 == 0: 
        l = acquire_length_of_chain(n / 2)
        if n / 2 < given:
            d[n / 2] = l
    else:
        l = acquire_length_of_chain(3 * n + 1)
        if 3 * n + 1 < given:
            d[3 * n + 1] = l
    return l + 1

start = time()
answer = 0
maxlength = 0
for i in range(1, given + 1):
    d[i] = acquire_length_of_chain(i)
    if maxlength < d[i]:
        maxlength = d[i]
        answer = i
end = time()
print answer, end - start

# 2
start = time()
given = 1000000
answer = 0
maxlength = 0
n = [True] * (given + 1)
for i in range(given, 0, -1):
    if n[i] == False:
        continue
    n[i] = False
    current = i
    currentlength = 1
    while current != 1:
        if current % 2 == 0:
            current = current / 2
        else:
            current = 3 * current + 1
        currentlength = currentlength + 1
        if current >= 1 and current < given:
            n[current] = False
    if currentlength > maxlength:
        maxlength = currentlength
        answer = i
end = time()
print answer, end - start

# 1
start = time()
given = 1000000
maxlength = 0
answer = 0
for i in range(1, given):
    current = i
    currentlength = 1
    while current != 1:
        if current % 2 == 0:
            current = current / 2
        else:
            current = 3 * current + 1
        currentlength = currentlength + 1
    if currentlength > maxlength:
        maxlength = currentlength
        answer = i
end = time()
print answer, end - start
