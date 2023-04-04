# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 18:28:02 2021

@author: Matteo
"""

def T(n):
    tot = 0
    for i in range(1, int(n**0.5)+1):
        tot += issquareS(i) * i**2
    return tot

def issquareS(n):
    s = n**2
    for splitting in splittings(str(s)):
        if sum([int(i) for i in splitting]) == s:
            return True
    return False

def splittings(s):
    splits = [] 
    for i in range(len(s)):
        splits += [[s[:i]]+l for l in splittings(s[i:])]
    return splits

if __name__ == "__main__":
    print(T(10**4))
        