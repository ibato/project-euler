# -*- coding:utf-8 -*-

from time import *
from math import *

start = time()

f = open("textfiles/keylog.txt", "r")
replies = sorted(list(set([r.rstrip() for r in f.readlines()])))

print len(replies)
print replies

# 파일을 읽어서 위와 같이 중복 제거, 소팅하면 33개의 수가 남는다.
# 소팅한 결과를 토대로 pensil and paper 로 답을 구한다.

end = time()

print end - start
