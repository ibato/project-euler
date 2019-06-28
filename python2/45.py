from time import *
from util import *

start = time()
answer = 0

n = 144
while True:
    h = n * (2 * n - 1)
    if is_pentagonal(h) and is_triangle(h):
        answer = h
        break
    n = n + 1

end = time()
print answer, end - start
