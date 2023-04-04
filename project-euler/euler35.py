# -*- coding: utf-8 -*-

from utils import isprime, rotate, index, number_from_list, getdigits

primes = []
for i in range(2,1000000):
    if isprime(i):
        primes.append(i)
        
def check_circular(primes, n):
    l = getdigits(n)
    for i in rotate(l):
        tmp = number_from_list(i)
        if index(primes, tmp) == -1:
            return False
    return True

res = []
for i in primes:
    if check_circular(primes, i):
        res.append(i)
    

