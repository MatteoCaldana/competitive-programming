# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 20:13:45 2021

@author: Matteo
"""

import time


def stupid(n):
    return sum([i**i for i in range(1, n+1)])

def cutpow(a,b):
    res = 1
    for _ in range(b):
        res = int(str(res*a)[-10:])
    return res

def logpow(a, b):
    res = 1
    while (b > 0):
        if (b & 1):
            res *= a
        a *= a
        b >>= 1
    return res

def cutlogpow(a, b):
    res = 1
    while (b > 0):
        if (b & 1):
            res = int(str(res*a)[-10:])
        a = int(str(a*a)[-10:])
        b >>= 1
    return res

def notstupid(n):
    return sum([logpow(i,i) for i in range(1, n+1)])

start_time = time.time()

print(notstupid(1000))

print("--- %s seconds ---" % (time.time() - start_time))

