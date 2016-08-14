from time import *
from math import *

start = time()
answer = 0
f = open("textfiles/words.txt", "r")
words = f.read().replace("\"", "").split(",")
print len(filter(lambda v: sqrt(1 + 8 * v) == int(sqrt(1 + 8 * v)), [reduce(lambda x, y: x + y, [ord(w[i]) - ord('A') + 1 for i in range(len(w))]) for w in words])), time() - start
