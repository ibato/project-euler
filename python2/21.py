from time import *
from math import *
from divisor import *

# 1
start = time()
answer = 0
amicable = [0] * 10000
for i in range(1, 10000):
    amicable[i] = acquire_sum_of_proper_divisors(i)
    if amicable[i] < i and amicable[amicable[i]] == i:
        answer = answer + i + amicable[i]
end = time()
print answer, end - start

# 2
start = time()
answer = 0
for i in range(1, 10000):
    sum1 = acquire_sum_of_proper_divisors(i)
    sum2 = acquire_sum_of_proper_divisors(sum1)
    if (i == sum2) and (i < sum1):
        answer = answer + i + sum1
end = time()
print answer, end - start
