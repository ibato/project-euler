from time import *

start = time()
answer = 0
a = 2 # denominator
b = 3 # numerator
for i in range(999):
    c = a + b # denominator
    d = 2 * a + b # numerator
    a = c
    b = d
    if len(str(b)) > len(str(a)):
        answer = answer + 1
end = time()
print answer, end - start
