# -*- coding: utf-8 -*-

from utils import fact, getdigits
import time
import numpy as np

limit = 1000

def fill(fun, limit):
    res = []
    for i in range(limit):
        res.append(fun(i))
    return res

def tfact(limit):
    res = [1]
    for i in range(1,limit):
        res.append(res[-1]*i)
    return res

def f(n):
    return sum([fact(i) for i in getdigits(n)])

def f_t(n, t_fact, t_dig):
    return sum([t_fact[i] for i in t_dig[n]])

def sf(n):
    return sum(getdigits(f(n)))

def sf_t(n, t_f, t_dig):
    return sum(t_dig[t_f[n]])
    
def g(i):
    for n in range(1000000000000):
        if sf(n) == i:
            return n
    raise ValueError

def sg(i):
    return sum([int(j) for j in str(g(i))])

start_time = time.time()
res = fill(sf, limit)
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()

digit_sum_limit = 2000000
digit_sum_table = np.array([0,1,2,3,4,5,6,7,8,9]+[0]*(digit_sum_limit-10))
for i in range(10, digit_sum_limit):
    digit_sum_table[i] = digit_sum_table[i//10] + i%10
    
f_limit = 100000
f_table = np.array([fact(i) for i in range(10)]+[0]*(f_limit-10))
for i in range(10, f_limit):
    f_table[i] = f_table[i//10] + f_table[i%10]
    
sf_limit = 100000
sf_table = np.array([0]*sf_limit)
for i in range(sf_limit):
    sf_table[i] = digit_sum_table[f_table[i]]

def digit_sum(n):
    if n < digit_sum_limit:
        return digit_sum_table[n]
    return n%10 + digit_sum(n//10)

def fact_digit_sum(n):
    if n < f_limit:
        return f_table[n]
    return f_table[n%10] + fact_digit_sum(n//10)

def sf_sum(n):
    return digit_sum(fact_digit_sum(n))

print("--- %s seconds ---" % (time.time() - start_time))

m = 0
for i in range(3*10**25-100001,3*10**25+100001):
    tmp = sf_sum(i)
    if tmp > m:
        m = tmp
        print(i, m)









