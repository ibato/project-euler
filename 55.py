from time import *
from util import *

def is_lychrel(num):
    for i in range(50):
        num = num + int(str(num)[::-1])
        if is_palindrome(num):
            return False
    return True

start = time()
answer = sum([1 for i in range(1, 10000) if is_lychrel(i)])
end = time()
print answer, end - start
