from time import *
from math import *
from divisor import *

start = time()
n = 1
answer = 0
while True:
    triangle = n * (n + 1) / 2
    if n % 2 == 0:
        # n / 2, (n + 1) 
        count1 = acquire_num_of_divisors(n / 2)
        count2 = acquire_num_of_divisors(n + 1)
    else:
        # n, (n + 1) / 2
        count1 = acquire_num_of_divisors(n)
        count2 = acquire_num_of_divisors((n + 1) / 2)
    n = n + 1
    if count1 * count2 > 500:
        answer = triangle
        break
end = time()
print answer, end - start

start = time()
n = 1
answer = 0
while True:
    triangle = n * (n + 1) / 2
    count = 0
    for i in range(1, int(sqrt(triangle)) + 1):
        if triangle % i == 0:
            count = count + 1
    if count * 2 > 500:
        answer = triangle
        break
    n = n + 1
end = time()
print answer, end - start
