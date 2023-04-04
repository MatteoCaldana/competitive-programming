# -*- coding: utf-8 -*-

from utils import list_divisors, index
from factorize import fill_primes, fill_divisors
import time
import numpy as np

limit = 100

start_time = time.time()
primes = np.array(fill_primes(limit))
divisors = np.array(fill_divisors(limit))
sum_div = np.array([sum(divisors[i])-i for i in range(len(divisors))])

to_check = list(set(range(1,limit)) - set(primes))
print("--- %s seconds ---" % (time.time() - start_time))

print(len(to_check))

def amicable_chain(n, limit):
    chain = []
    curr = n
    while curr not in chain:
        if curr == 1 or curr >= limit:
            chain = []
            break
        chain.append(curr)
        curr = sum_div[curr]
    return chain

res = []
res_len = []

start_time = time.time()
for i in range(2,limit):
    if i in to_check:
        tmp = amicable_chain(i, limit)
        res.append(tmp)
        res_len.append(len(tmp))
        for j in tmp:
            idx = index(to_check, j)
            if idx != -1:
                del to_check[idx]
    if i % 1000 == 0:
        print(i,max(res_len))
print("--- %s seconds ---" % (time.time() - start_time))

    

    