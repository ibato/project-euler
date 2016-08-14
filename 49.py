from prime import *
from time import *
from itertools import *

start = time()
answer = 0
primes = acquire_primes(1000, 9999)
for prime in primes:
    c = combinations(permutations([x for x in str(prime)]), 3)
    for each in c:
        first = int(reduce(lambda x, y: x + y, each[0]))
        second = int(reduce(lambda x, y: x + y, each[1]))
        third = int(reduce(lambda x, y: x + y, each[2]))
        if first > 1000 and second > first and third > second:
            if first + third == 2 * second and is_prime(first) and is_prime(second) and is_prime(third):
                if not first == 1487:
                    answer = str(first) + str(second) + str(third)
                    break
        if not answer == 0:
            break
end = time()
print answer, end - start
