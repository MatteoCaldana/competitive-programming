# -*- coding: utf-8 -*-

#1504170715041707n mod 4503599627370517
from mod import Mod
import time 

a = 1504170715041707
mod = 4503599627370517

inv = (Mod(a, mod)**-1).n

#find all the coins for n smaller than limit
def brute_solve(limit):
    res = []
    
    MIN, old = a + 1, 0
    for n in range(1, limit):
        r = (old + a) % mod
        old = r
        if r < MIN:
            MIN = r
            res.append((n, MIN))
            print(n, MIN)
    return res

#search for an Eulercoin smaller than coin for n greater than n
def inv_search(n, coin):
    coin -= 1 # strictly smaller than coin, otherwise returns coin
    
    MIN, mem_coin, mem_n = a, coin, n
    while coin > 0:
        curr_n = (coin*inv) % mod
        diff = curr_n - n
        #print(curr_n, n, curr_n - n > 0)
        if diff < MIN:
            MIN = diff
            mem_n = curr_n
            mem_coin = coin
            
        coin -= 1
 
    return mem_n, mem_coin

#iterate inv_search for coins smaller than coin and n bigger than n
def inv_solve(n, coin):
    res = [(n, coin)]
    while res[-1][1] > 1:
        res.append(inv_search(*res[-1]))
        print(*res[-1])
        
    return res[1:] #do not return the element passed to the function


start_time = time.time() 
res = brute_solve(int(a**.5)+1)
res += inv_solve(*res[-1])
result = sum([i[1] for i in res])
print("--- %s seconds ---" % (time.time() - start_time))


