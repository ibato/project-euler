import math
import operator as op

def nCr_v1(n, r):
    rfactorial = 1;
    for i in range(1, r + 1):
        rfactorial = rfactorial * i
    nPr = 1;
    for i in range(n - r + 1, n + 1):
        nPr = nPr * i
    return nPr / rfactorial

def nCr_v2(n, r):
    r = min(r, n-r)
    if r == 0: 
        return 1
    num = reduce(op.mul, xrange(n, n - r, -1))
    denom = reduce(op.mul, xrange(1, r + 1))
    return num / denom

def nCr_v3(n, r):
    f = math.factorial
    return f(n) / (f(r) * f(n-r))
