# -*- coding: utf-8 -*-

from itertools import permutations
from utils import number_from_list, isprime

res = []
for n_digit in range(2,11):
    for i in permutations(list(range(1,n_digit))):
        n = number_from_list(i)
        if isprime(n):
            res.append(n)