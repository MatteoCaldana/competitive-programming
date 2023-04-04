# -*- coding: utf-8 -*-

from utils import isprime

limit = 100000
odds = list(range(1,limit,2))
composite_odds = odds.copy()
primes = []
squares = []

for i in odds:
    if isprime(i):
        composite_odds.remove(i)
        primes.append(i)
        
i = 1
while i*i < limit:
    squares.append(i*i)
    i += 1
    
        
def isGoldbach(n):
    i = 0
    while n - 2*squares[i] > 0:
        if isprime(n - 2*squares[i]):
            return True
        i += 1
    return False

for i in composite_odds:
    if not isGoldbach(i):
        print(i)
