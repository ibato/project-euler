from time import *

# 2
start = time()
answer = 0
for n in range(1, 22):
    for i in range(1, 10): # 10^n is (n+1) digits
        if (len(str(i ** n)) == n):
            answer = answer + 1
end = time()
print answer, end - start

# 1
# paper and pencel
