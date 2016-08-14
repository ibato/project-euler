from time import *
from prime import *

# all numbers
start = time()
count = 0
n = 1
while True:
    n = n + 1
    if is_prime(n) == True:
        count = count + 1
        if count == 10001:
            break;
end = time()
print n, end - start

# end with 1, 3, 7, 9
start = time()
count = 1
n = 1
while True:
    n = n + 2
    if n % 5 == 0:
        continue
    if is_prime(n) == True:
        count = count + 1
        if count == 10000: # because we do not count 2
            break;
end = time()
print n, end - start
