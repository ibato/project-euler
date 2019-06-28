from time import *

start = time()
a = 1
b = 2
summation = b
while a + b < 4000000:
    c = a + b
    if c % 2 == 0:
        summation = summation + c
    a = b
    b = c
end = time()
print summation, end - start
