from time import *

start = time()
summation = 0
for i in range(1, 1001):
    summation = summation + pow(i, i)
divisor = pow(10, 10)
end = time()
print summation % divisor, end - start
