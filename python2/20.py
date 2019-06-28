from time import *
from math import *

# 1
start = time()
answer = reduce(lambda x, y: x + y, [int(i) for i in str(reduce(lambda x, y: x * y, range(1, 100)))])
end = time()
print answer, end - start

# 2
start = time()
answer = sum([int(x) for x in str(factorial(100))])
end = time()
print answer, end - start
