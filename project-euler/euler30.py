# -*- coding: utf-8 -*-

from utils import getdigits

result = 0
# 9**5*7 = 413343 < 1e7413343
for i in range(2,1000000):
    dig = getdigits(i)
    res = sum([j**5 for j in dig])
    if i == res:
        print(i)
        result += i