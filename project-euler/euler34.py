# -*- coding: utf-8 -*-

from utils import fact, getdigits, getndigits

def digit_factorial(n):
    return sum([fact(i) for i in getdigits(n)]) == n

res = []
for i in range(3,fact(9)*getndigits(fact(9))):
    if i % 100000 == 0:
        print(i)
    if digit_factorial(i):
        res.append(i)
    
result = sum(res)


