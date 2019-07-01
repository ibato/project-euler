# %% [markdown]
## is_prime()
# Check all odd numbers from 3 to $\sqrt{n}$, so the complexity is $O(\sqrt{n})$.

# %%
from math import sqrt
from time import time


def is_prime(n):
    if n <= 1:
        return False
    if n != 2 and n % 2 == 0:
        return False
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def test():
    assert is_prime(32416190071) == True
    assert is_prime(4) == False


start = time()
test()
print("Execution time:", time() - start)
