from itertools import *
from time import *
from util import *

# 3
start = time()
answer = []
for multiplicand in range(1, 10000):
    for multiplier in range(1, 10000 / multiplicand):
        if is_pandigital(str(multiplicand) + str(multiplier) + str(multiplicand * multiplier), "123456789"):
            answer.append(multiplicand * multiplier)
end = time()
print reduce(lambda x, y: x + y, set(answer)), end - start

# 2
start = time()
answer = []
for multiplicand in range(1, 10000):
    for multiplier in range(1, 10000 / multiplicand):
        if is_pandigital(str(multiplicand) + str(multiplier) + str(multiplicand * multiplier), "123456789"):
            if multiplicand * multiplier not in answer:
                answer.append(multiplicand * multiplier)
end = time()
print reduce(lambda x, y: x + y, answer), end - start

# 1
start = time()
p = permutations(['1', '2', '3', '4', '5', '6', '7', '8', '9'])
answer = []
for d in p:
    for i in xrange(0, 3):
        for j in xrange(i + 1, 5):
            multiplicand = int("".join(d[0:i + 1]))
            multiplier = int("".join(d[i + 1:j + 1]))
            product = int("".join(d[j + 1::]))
            if multiplicand * multiplier == product and product not in answer:
                answer.append(product)
end = time()
print reduce(lambda x, y: x + y, answer), end - start
