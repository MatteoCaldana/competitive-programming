# -*- coding: utf-8 -*-

from utils import getdigits

res = []
for i in range(200000):
    res += getdigits(i)

result = res[1] * res[10] * res[100] * res[1000] * res[10000] * res[100000] * res[1000000]

result = 1
for i in range(0,7):
    result *= res[10**i]