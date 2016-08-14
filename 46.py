from time import *
from math import *
from prime import *

def is_not_satisfy_conjecture(n):
    for i in range(n):
        if is_prime(i) == True:
            j = sqrt((n - i) / 2)
            if j == int(j):
                return False
    return True

start = time()
answer = 0
n = 3
while True:
    if is_prime(n) == False and is_not_satisfy_conjecture(n):
        answer = n
        break
    n = n + 2
    if n % 5 == 0:
        n = n + 2

end = time()
print answer, end - start
