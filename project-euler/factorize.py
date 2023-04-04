# -*- coding: utf-8 -*-

from utils import index
import numpy as np

def isprime_table(primes, n):
    bound = int(n**0.5)
    i = 0
    while primes[i] <= bound:
        if n % primes[i] == 0:
            return False
        i += 1
    return True

def fill_primes(limit):
    primes = [2, 3, 5, 7]
    for i in range(11,limit,2):
        if isprime_table(primes, i):
            primes.append(i)
    return primes

def factorize(primes, factorizations, n):
    if index(primes, n) != -1:
        factorizations.append({n:1})
        return
    
    for i in primes:
        if n % i == 0:
            div = n // i
            tmp = factorizations[div].copy()
            if i in tmp:
                tmp[i] += 1
            else:
                tmp[i] = 1
            factorizations.append(tmp)
            return
        
def fill_factorizations(limit):
    factorizations = [{}, {1:1}]
    primes = fill_primes(limit)
    for i in range(2,limit):
        factorize(primes, factorizations, i)
    return factorizations

def list_divisiors(primes, divisors, n):
    if index(primes, n) != -1:
        divisors.append(set([1, n]))
        return
    
    for i in primes:
        if n % i == 0:
            div = n // i
            tmp = divisors[div].copy()
            tmp2 = set()
            for j in tmp:
                tmp2.add(j*i)
            divisors.append(tmp|tmp2)
            return

def fill_divisors(limit):
    divisors = [set(), set([1])]
    primes = fill_primes(limit)
    for i in range(2,limit):
        list_divisiors(primes, divisors, i)
    return divisors
    










