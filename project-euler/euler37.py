# -*- coding: utf-8 -*-

from utils import getdigits, number_from_list, isprime

def left_truncable(n):
    l = getdigits(n)
    for i in range(len(l)):
        if not isprime(number_from_list(l[i:])):
            return False
    return True

def right_truncable(n):
    l = getdigits(n)
    for i in range(len(l)):
        if not isprime(number_from_list(l[:len(l)-i-1])):
            return False
    return True

def istruncable(n):
    return left_truncable(n) and right_truncable(n)

res = []
for i in range(8,1000000):
    if istruncable(i):
        res.append(i)
        
result = sum(res)