# -*- coding: utf-8 -*-

from factorize import fill_primes
from utils import index

primes = fill_primes(1000000)

for n in range(21,1000000):
    if sum(primes[:n]) > 1000000:
        break
    
# n = 547
        
for i in range(n-1,1,-1):
    s = sum(primes[:i])
    if index(primes, s) != -1:
        print(i, sum(primes[:i]))
        break
    
# at least 536 consecutives, sum greater than 958577

for offset in range(1,n-i):
    for j in range(n-1,i,-1):
        s = sum(primes[offset:j+offset])
        if index(primes, s) != -1:
            print(j, sum(primes[offset:j+offset]), offset)
            break        