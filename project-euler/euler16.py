# -*- coding: utf-8 -*-

from utils import getdigit, getndigits

n = 2**1000
n_dig = getndigits(n)

res = 0

for i in range(1, n_dig+1):
    res += getdigit(n, i)

