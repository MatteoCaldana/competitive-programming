# -*- coding: utf-8 -*-

from utils import getdigits

possible_pan_product = []

for i in range(2000,10000):
    if len(set(getdigits(i))) == 4:
        possible_pan_product.append(i)
        
def determine_pan(n):
    dig = getdigits(n)
    res = []
    for i in range(2,100): #5 digits in the multiplicand+multiplier -> the smallest has at most 2 digits
        if n % i == 0:
            tmp = set(getdigits(i) + getdigits(n//i) + dig)
            if (len(tmp) == 9) and (0 not in tmp):
                res.append((i, n//i, n))
    return res

tmp = []          
for i in possible_pan_product:
    tmp += determine_pan(i)
    
result = sum(set([i[2] for i in tmp]))