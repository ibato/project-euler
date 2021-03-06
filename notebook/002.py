# %% [markdown]
# Even Fibonacci numbers
# https://projecteuler.net/problem=2
#
# > Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
# >
# > 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

# %%
from time import time


def solve():
    a = 1
    b = 2
    summation = b
    while a + b < 4000000:
        c = a + b
        if c % 2 == 0:
            summation = summation + c
        a = b
        b = c
    return summation


def test():
    answer = solve()
    print("Answer:", answer)
    assert answer == 4613732


start = time()
test()
print("Execution time:", time() - start)
