# -*- coding: utf-8 -*-

from utils import isprime

l = [2]

for i in range(3,2_000_000 + 1, 2):
    print(i)
    if isprime(i):
        l.append(i)

res = sum(l)
