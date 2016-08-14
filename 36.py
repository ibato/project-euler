from time import *
from util import *

start = time()
answer = 0
for i in range(1, 1000000, 2):
    decimal = str(i)
    binary = str(bin(i))[2::]
    if is_palindrome(decimal) == True and is_palindrome(binary) == True:
        answer = answer + i
end = time()
print answer, end - start
