# -*- coding: utf-8 -*-

from utils import fact, getdigit, getndigits

n = fact(100)

res = 0

for i in range(1, getndigits(n)+1):
    res += getdigit(n,i)

