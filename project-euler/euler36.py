# -*- coding: utf-8 -*-

from utils import getdigits, number_from_list

def palindromiclist(l):
    for i in range(len(l) // 2):
        if l[i] != l[len(l)-i-1]:
            return False
    return True

def ispalindromic(n):
    return palindromiclist(getdigits(n))

def list_base_change(n, b):
    l = []
    while n != 0:
        l.append(n % b)
        n = n // b
    return l

def is_double_based_palindrome(n):
    return ispalindromic(n) and palindromiclist(list_base_change(n, 2))

res = []
for i in range(1000000):
    if is_double_based_palindrome(i):
        res.append(i)
        
result = sum(res)
        