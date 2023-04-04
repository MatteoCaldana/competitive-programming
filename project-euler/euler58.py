# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

import operator
import numpy as np
from factorize import fill_primes
from utils import index, isprime

limit = 10**7

#primes = fill_primes(10000000)

def syntetic_spiral(n):
    layer = 1
    circle_size = 1
    curr_circle_size = 0
    edge_size = 0
    diag = []
    for i in range(1,n):
        if i % 100000 == 0:
            print(i)
        edges = [circle_size-3*edge_size-1, circle_size-2*edge_size-1, circle_size-edge_size-1, circle_size-1]
        if curr_circle_size in edges:
            diag.append(i)
        
        if curr_circle_size == circle_size:
            curr_circle_size = 0
            layer += 1
            edge_size = 2*(layer - 1)
            circle_size = 4*edge_size
        
        curr_circle_size += 1  
    return diag

def prime_frac(d):
    n_primes = 0
    for i in range(len(d)):
        if i % 100 == 0:
            print(i)
        if isprime(d[i]):
            n_primes += 1
    print(n_primes, len(d))
    return n_primes / len(d)

n = 11
f = prime_frac(syntetic_spiral(n**2))



