# -*- coding: utf-8 -*-

from utils import list_divisors

triangular = 1
n_div = 1
i = 2

while n_div < 501:
    print(i, triangular, n_div)
    triangular += i
    i += 1
    n_div = len(list_divisors(triangular))

print(i, triangular, n_div)