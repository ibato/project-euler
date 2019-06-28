from time import *

# 1
def is_answer(num):
    l = [x for x in str(num)]
    for i in range(1, 6):
        if sorted(l) != sorted([x for x in str(num * i)]):
            return False
    return True

start = time()
answer = 0
i = 0
while True:
    i = i + 1
    if is_answer(i):
        answer = i
        break
end = time()
print answer, end - start

# 2
# 1/7
