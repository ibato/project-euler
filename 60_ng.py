from time import *
from prime import *
from itertools import *

start = time()
answer = []
primes = acquire_primes(2, 7500)
primes.remove(2)
primes.remove(5)

for c1 in combinations(primes, 4):
    if c1[0] > 25: break
    flag = True
    for c2 in combinations(c1, 2):
        n1 = int(str(c2[0]) + str(c2[1]))
        n2 = int(str(c2[1]) + str(c2[0]))
        if is_prime(n1) == False or is_prime(n2) == False:
            flag = False
            break
    if flag == True:
        answer.append(c1)
        print "answer1: ", c1

primes = acquire_primes(17, 25000)

for a in answer:
    for p in primes:
        a = a + (p,)
        flag = True
        for c in combinations(a, 2):
            n1 = int(str(c[0]) + str(c[1]))
            n2 = int(str(c[1]) + str(c[0]))
            if is_prime(n1) == False or is_prime(n2) == False:
                flag = False
                break
        if flag == True:
            print "answer2: ", a, sum(a)
        a = a[:-1]
end = time()
print end - start

# 13 5197 5701 6733 8389 
