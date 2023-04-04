# -*- coding: utf-8 -*-

import time 
from utils import isprime, getdigits
from factorize import fill_primes

start_time = time.time()
primes = fill_primes(10000)
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
primes = []
for i in range(1000,10000):
    if isprime(i):
        primes.append(i)
print("--- %s seconds ---" % (time.time() - start_time))

digits = {}

for i in primes:
    digs = getdigits(i)
    digs.sort()
    digs = tuple(digs)
    if digs in digits:
        digits[digs].append(i)
    else:
        digits[digs] = [i]

def check_diff(l):
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[j] - l[i] == 3330:
                return True
    return False

res = []       
for key, value in digits.items():
    if len(value) >= 3:
        if max(value) - min(value) >= 6660: 
            if check_diff(value):
                res.append(value)
                
                









    

