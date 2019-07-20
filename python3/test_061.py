from itertools import permutations
from functools import reduce
import test_polygonal as pg 
import test_prime as prm
import test_runner as runner


def solve():
    answer = 0

    nt = len(pg.find_triangles(1, 1000))
    ns = len(pg.find_squares(1, 1000))
    np = len(pg.find_pentagonals(1, 1000))
    nhex = len(pg.find_hexagonals(1, 1000))
    nhep = len(pg.find_heptagonals(1, 1000))
    no = len(pg.find_octagonals(1, 1000))

    triangle = pg.find_triangles(1000, 10000)
    square = pg.find_squares(1000, 10000)
    pentagonal = pg.find_pentagonals(1000, 10000)
    hexagonal = pg.find_hexagonals(1000, 10000)
    heptagonal = pg.find_heptagonals(1000, 10000)
    octagonal = pg.find_octagonals(1000, 10000)

    arr = [triangle, square, pentagonal, hexagonal, heptagonal, octagonal]

    for p in permutations(range(6), 6):
        for a in range(len(arr[p[0]])):
            first_a = str(arr[p[0]][a])[:2]
            last_a = str(arr[p[0]][a])[2:]
            for b in range(len(arr[p[1]])):
                first_b = str(arr[p[1]][b])[:2]
                last_b = str(arr[p[1]][b])[2:]
                if last_a == first_b:
                    for c in range(len(arr[p[2]])):
                        first_c = str(arr[p[2]][c])[:2]
                        last_c = str(arr[p[2]][c])[2:]
                        if last_b == first_c:
                            for d in range(len(arr[p[3]])):
                                first_d = str(arr[p[3]][d])[:2]
                                last_d = str(arr[p[3]][d])[2:]
                                if last_c == first_d:
                                    for e in range(len(arr[p[4]])):
                                        first_e = str(arr[p[4]][e])[:2]
                                        last_e = str(arr[p[4]][e])[2:]
                                        if last_d == first_e:
                                            for f in range(len(arr[p[5]])):
                                                first_f = str(arr[p[5]][f])[:2]
                                                last_f = str(arr[p[5]][f])[2:]
                                                if last_e == first_f and last_f == first_a:
                                                    if a != b and a != c and a != d and a != e and a != f and b != c and b != d and b != e and b != f and c != d and c != e and c != f and d != e and d != f and e != f:
                                                        answer = reduce(lambda x, y: x + y, [arr[p[0]][a], arr[p[1]][b], arr[p[2]][c], arr[p[3]][d], arr[p[4]][e], arr[p[5]][f]])
                                                        print(arr[p[0]][a], arr[p[1]][b], arr[p[2]][c], arr[p[3]][d], arr[p[4]][e], arr[p[5]][f], answer)
                                                        return answer


def test():
    right_answer = 28684
    runner.run(solve, right_answer)


if __name__ == '__main__':
    test()
