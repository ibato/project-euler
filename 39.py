from time import *
from math import *

def acquire_num_of_solution(p):
    count = 0
    for z in range(p / 2, p / 3, -1):
        for x in range(1, z / 2):
            y = p - x - z
            if z * z == x * x + y * y: 
                count = count + 1
    return count

start = time()
answer = 0
maximum = 0
for p in range(1000, 12, -1):
    n = acquire_num_of_solution(p)
    if maximum < n:
        maximum = n
        answer = p
end = time()
print answer, end - start
