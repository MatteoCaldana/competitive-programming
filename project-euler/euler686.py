# -*- coding: utf-8 -*-

import time
from utils import getdigits

def p(L, n):
    pattern = str(L)
    i = 0
    while n > 0:
        curr = 2**i
        if str(curr)[:len(pattern)] == pattern:
            print(i,str(curr)[:20])
            n -= 1
        i += 1
    return i - 1

def pp(n):
    i = 89
    curr = 2**i
    n_dig = len(str(curr))
    tmp1 = 10**n_dig
    tmp2 = 10**(n_dig-3)
    while n > 0:
        if curr // tmp1 > 0:
            curr //= 10
        if curr // tmp2 == 123:
            if n % 1000 == 0:
                print(n)
            n -= 1
        
        curr *= 2
        i += 1
    return i - 1


start_time = time.time()
#p(123,45)
r=pp(678910)
print("--- %s seconds ---" % (time.time() - start_time))
