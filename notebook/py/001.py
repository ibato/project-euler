# %% [markdown]
# Multiples of 3 and 5
# https://projecteuler.net/problem=1
#
# > If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# >
# > Find the sum of all the multiples of 3 or 5 below 1000.

# %% [markdown]
# It's just the brute force attack.

# %%
from time import time


def solve():
    return sum(filter(lambda x: x % 3 == 0 or x % 5 == 0, range(1, 1000)))


def test():
    answer = solve()
    print("Answer:", answer)
    assert answer == 233168


start = time()
test()
print("Execution time:", time() - start)
