# -*- coding: utf-8 -*-

from factorize import fill_primes
from utils import getdigits

primes = fill_primes(1000000)

def count_dig(l):
    res = [0]*10
    for i in l:
        res[i] += 1
    return res

digits = []
counts = []
maxs = []
for i in primes:
    digits.append(getdigits(i))
    counts.append(count_dig(digits[-1]))
    maxs.append(max(counts[-1]))

res = []
for i in range(len(maxs)):
    if maxs[i] >= 4 and primes[i] > 100000:
        res.append(primes[i])
        
