from time import *
from sys import *
from math import *
from util import *

start = time()
answer = maxint
n = 1
while True:
    n = n + 1
    for k in range(1, n / 2 + 1):
        smaller = (k * (3 * k - 1)) / 2
        bigger = ((n - k) * (3 * (n - k) - 1)) / 2
        if is_pentagonal(bigger + smaller) and is_pentagonal(bigger - smaller):
            answer = bigger - smaller
            break
    if answer != maxint: 
        break
end = time()
print answer, end - start
