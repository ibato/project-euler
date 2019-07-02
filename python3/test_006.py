from time import time
import test_runner as runner

# 006. Sum square difference
# https://projecteuler.net/problem=6


# Pencel and Paper
#
# (1+2+...+100)^2-(1^2+2^2+...+100^2)
# = ((100*101)/2)^2-(100*101*201)/6
# = 25502500-338350
# = 25165150
def solve():
    return 25164150


def test():
    right_answer = 25164150
    runner.run(solve, right_answer)


if __name__ == '__main__':
    test()
