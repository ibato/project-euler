from time import *

def find_other_cubes(c, cube):
    return [d for d in cube if sorted(str(c)) == sorted(str(d)) and c != d]

start = time()

n = 5

# 216, 464 (inclusive)
# 465, 999
# 1000, 4641
# 4642, 9999
# 10000, ...
cube = [i * i * i for i in range(4643, 10000)]
#for i in range(4643, 11000):
#    print i, i * i * i, len(str(i * i * i))
# print len(str(4643 * 4643 * 4643))

for i in range(len(cube)):
    ret = find_other_cubes(cube[i], cube)
    if len(ret) == n - 1:
        print cube[i], ret
    if i % 1000 == 1:
        print "i'm alive", i, cube[i]

end = time()

print end - start
