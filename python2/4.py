from time import *
from util import *

start = time()
answer = 0
for i in range(999, 100, -1):
    for j in range(999, 100, -1):
        if i != j:
            if is_palindrome(i * j) == True and answer < (i * j):
                answer = i * j
end = time()
print answer, end - start

# a * 100000 + b * 10000 + c * 1000 + d * 100 + e * 10 + f
# if palindrome,
# a * 100000 + b * 10000 + c * 1000 + c * 100 + b * 10 + a
# = a * 100001 + b * 10010 + c * 1100
# = 11(9091a + 910b + 100c)

start = time()
answer = 0
for i in range(999, 100, -1):
    for j in range(999, 100, -1):
        if (i * j) % 11 == 0 :
            if is_palindrome(i * j) == True and answer < (i * j):
                answer = i * j
end = time()
print answer, end - start

