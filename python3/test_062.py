from itertools import permutations
from functools import reduce
import test_polygonal as pg 
import test_prime as prm
import test_runner as runner


# 216, 464 (inclusive)
# 465, 999
# 1000, 4641
# 4642, 9999
# 10000, ...
cube = [i * i * i for i in range(4643, 10000)]
n = 5


def solve():
    for i in range(len(cube)):
        ret = find_other_cubes(cube[i], cube)
        if len(ret) == n - 1:
            print(cube[i], ret)
            return cube[i]


def find_other_cubes(c, cube):
    return [d for d in cube if sorted(str(c)) == sorted(str(d)) and c != d]


def test():
    right_answer = 127035954683
    runner.run(solve, right_answer)


if __name__ == '__main__':
    test()
