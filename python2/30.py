from time import *

# 1
start = time()
answer = 0
for a in range(10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                for e in range(10):
                    for f in range(10):
                        n = f + e * 10 + d * 100 + c * 1000 + b * 10000 + a * 100000
                        sumofpowers = (a ** 5) + (b ** 5) + (c ** 5) + (d ** 5) + (e ** 5) + (f ** 5)
                        if n == sumofpowers:
                            answer = answer + n
end = time()
print answer - 1, end - start

# 2
start = time()
answer = 0
for i in range(2, 354294):
    sumofpowers = 0
    for j in str(i):
        sumofpowers = sumofpowers + (int(j) ** 5)
    if sumofpowers == i:
        answer = answer + i
end = time()
print answer, end - start
