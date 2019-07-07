from time import time
from functools import reduce
import test_pandigital as pandigital
import test_runner as runner


def solve():
    md = 1
    mn = 1
    for denominator in range(11, 100):
        for numerator in range(10, denominator):
            if denominator % 10 == 0 or numerator % 10 == 0:
                continue
            d = str(denominator)
            n = str(numerator)
            for s in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                if s in d and s in n:
                    d2 = d.replace(s, '')
                    n2 = n.replace(s, '')
                    if len(d2) == 1 and len(n2) == 1:
                        if float(n2) / float(d2) == float(n) / float(d):
                            md = md * int(d2)
                            mn = mn * int(n2)
    for i in range(1, min(md, mn)):
        if md % i == 0 and mn % i == 0:
            md = md / i
            mn = mn / i
    return md


def test():
    right_answer = 100
    runner.run(solve, right_answer)


if __name__ == '__main__':
    test()
