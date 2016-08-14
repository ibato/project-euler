from combinatorics import *
from time import *

count = 0
for i in range(1, 101):
    if i % 7 == 0:
        count = count + 21 * (i / 7)
    if i % 49 == 0:
        pass

print count

#sum = 0
#for i in range(1, 101):
#    if i % 7 == 0:
#        sum = sum + 21 * (i / 7)
#    if i == 49:
#        sum = sum + 315
#print sum, 5050 - sum

for i in range(1, 101):
    count = 0
    for j in range(i):
        if nCr(i, j) % 7 == 0:
            count = count + 1
    print i, count
