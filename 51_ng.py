from time import *
from prime import *
from itertools import *

def acquire_patterns(digit):
    result = []
    for i in range(3, digit): # *:i, d:digit-i
        if i % 3 != 0:
            break
        pattern = ""
        for j in range(i):
            pattern = pattern + "*"
        for j in range(digit - i):
            pattern = pattern + "d"
        p = permutations(pattern)
        for each in p:
            if not each in result:
                result.append(each)
    return result

def acquire_answer(sieve, patterns, threshold):
    classified = []
    for i in range(len(patterns)):
        classified.append({})
    for prime in sieve:
        sprime = str(prime)
        for i in range(len(patterns)):
            key = ""
            same = ""
            for j in range(len(patterns[i])):
                if patterns[i][j] == "d":
                    key = key + sprime[j]
                elif same == "":
                    same = sprime[j]
                elif same != sprime[j]:
                    same = False
                    break
            if key not in classified[i].keys():
                classified[i][key] = []
            if not same == False:
                classified[i][key].append(sprime)
                if len(classified[i][key]) == threshold:
                    return classified[i][key][0]
    return "not exists"

start = time()
answer = 0
threshold = 8
digit = 1
while True:
    digit = digit + 1
    sieve = acquire_primes(int(pow(10, digit - 1)), int(pow(10, digit)))
    patterns = acquire_patterns(digit)
    print patterns
    answer = acquire_answer(sieve, patterns, threshold)
    if not answer == "not exists":
        break
end = time()
print answer, end - start
