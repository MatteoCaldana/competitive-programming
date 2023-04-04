# -*- coding: utf-8 -*-

from factorize import fill_factorizations
from fraction import Fraction
from functools import reduce

#table = fill_factorizations(int(1e6))

def relative_prime(n, m, table):
    return not len(set(table[n].keys()) & set(table[m].keys()))

def euler_totient(n, table):
    n_coprimes = 1
    for i in range(2, n):
        n_coprimes += relative_prime(n, i, table)
    return n_coprimes

def find_idx(l, perc):
    tmp = int(max(l)*perc)
    return [i for i in range(int(len(l))) if l[i] > tmp]

#heuristic1 = [len(i.keys()) for i in table]
#heuristic2 = [sum(i.values()) for i in table]
#heuristic3 = [reduce((lambda x, y: x * y), list(i.values())+[1]) for i in table]
#
#idx_h1 = find_idx(heuristic1,0.9)
#idx_h2 = find_idx(heuristic2,0.8)
#idx_h3 = find_idx(heuristic3,0.7)
#
#l = idx_h1 + idx_h2 + idx_h3
#
#rate, idx = 0, 0
#for i in l:
#    tmp = i/euler_totient(i, table)
#    print(i, tmp)
#    if tmp > rate:
#        rate, idx = tmp, i

###############################################################################

# using  fundamental theorem of arithmetic 
# https://en.wikipedia.org/wiki/Euler%27s_totient_function 
def euler_totient2(n, table):
    phi = n
    for i in table[n].keys():
        phi = phi * (1 - 1/i)
    return phi

def euler_totient3(n, table):
    phi = n
    for i in table[n].keys():
        phi = phi * (1 - 1/Fraction(i))
    return phi

rate, idx = 0, 0 
for i in range(2,int(1e6)):
    if i % 10000 == 0:
        print(i)
        
    tmp = i/euler_totient2(i, table)
    if tmp > rate:
        rate, idx = tmp, i



