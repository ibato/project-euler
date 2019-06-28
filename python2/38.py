from time import *
from util import *

start = time()
for i in range(9999, 2, -1):
    answer = ""
    for j in range(1, 10):
        answer = answer + str(i * j)
        if len(answer) >= 9:
            break
    if is_pandigital(answer, "123456789") == True:
        break
end = time()
print answer, end - start
