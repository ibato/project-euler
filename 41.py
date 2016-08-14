from time import *
from itertools import *
from prime import *

start = time()
p = permutations(['7', '6', '5', '4', '3', '2', '1'])
for each in p:
    joined = "".join(each)
    if is_prime(int(joined)) == True:
        answer = joined
        break
end = time()
print answer, end - start
