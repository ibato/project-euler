from time import *
from util import *
from itertools import *

start = time()

nt = len(acquire_triangle(1, 1000))
ns = len(acquire_square(1, 1000))
np = len(acquire_pentagonal(1, 1000))
nhex = len(acquire_hexagonal(1, 1000))
nhep = len(acquire_heptagonal(1, 1000))
no = len(acquire_octagonal(1, 1000))

triangle = acquire_triangle(1000, 10000)
square = acquire_square(1000, 10000)
pentagonal = acquire_pentagonal(1000, 10000)
hexagonal = acquire_hexagonal(1000, 10000)
heptagonal = acquire_heptagonal(1000, 10000)
octagonal = acquire_octagonal(1000, 10000)

arr = [triangle, square, pentagonal, hexagonal, heptagonal, octagonal]

for p in permutations(range(6), 6):
    for a in range(len(arr[p[0]])):
        first_a = str(arr[p[0]][a])[:2]
        last_a = str(arr[p[0]][a])[2:]
        for b in range(len(arr[p[1]])):
            first_b = str(arr[p[1]][b])[:2]
            last_b = str(arr[p[1]][b])[2:]
            if last_a == first_b:
                for c in range(len(arr[p[2]])):
                    first_c = str(arr[p[2]][c])[:2]
                    last_c = str(arr[p[2]][c])[2:]
                    if last_b == first_c:
                        for d in range(len(arr[p[3]])):
                            first_d = str(arr[p[3]][d])[:2]
                            last_d = str(arr[p[3]][d])[2:]
                            if last_c == first_d:
                                for e in range(len(arr[p[4]])):
                                    first_e = str(arr[p[4]][e])[:2]
                                    last_e = str(arr[p[4]][e])[2:]
                                    if last_d == first_e:
                                        for f in range(len(arr[p[5]])):
                                            first_f = str(arr[p[5]][f])[:2]
                                            last_f = str(arr[p[5]][f])[2:]
                                            if last_e == first_f and last_f == first_a:
                                                if a != b and a != c and a != d and a != e and a != f and b != c and b != d and b != e and b != f and c != d and c != e and c != f and d != e and d != f and e != f:
                                                    print arr[p[0]][a], arr[p[1]][b], arr[p[2]][c], arr[p[3]][d], arr[p[4]][e], arr[p[5]][f], reduce(lambda x, y: x + y, [arr[p[0]][a], arr[p[1]][b], arr[p[2]][c], arr[p[3]][d], arr[p[4]][e], arr[p[5]][f]])
                                                    print a, b, c, d, e, f
end = time()

print end - start
