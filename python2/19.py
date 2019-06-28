from time import *

start = time()
today = 1
# 1900
while today <= 366:
    today = today + 7
today = today % 365
# 1901 ~ 2000
answer = 0
year = 1901
normalmonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
abnormalmonth = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
while year <= 2000:
    month = normalmonth
    if year % 4 == 0: 
        month = abnormalmonth
    for i in range(12):
        while today < month[i]:
            today = today + 7
        today = today % month[i]
        if today == 2:
            answer = answer + 1
    year = year + 1
end = time()
print answer, end - start
