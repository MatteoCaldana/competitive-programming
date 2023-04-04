# -*- coding: utf-8 -*-

from factorize import fill_primes, factorize
from fraction import Fraction

limit = 40000000

primes_table = fill_primes(limit)
print("primes filled")
fact_table = [{}, {1:1}]
for i in range(2,limit):
    if i % 10000 == 0:
        print(i)
    factorize(primes_table, fact_table, i)
    
# using  fundamental theorem of arithmetic 
# https://en.wikipedia.org/wiki/Euler%27s_totient_function 
def euler_totient(n, table):
    phi = n
    for i in table[n].keys():
        phi = phi * (1 - 1/i)
    return int(round(phi))

def chain_lenght(n, table):
    length = 0
    while n != 1:
        n = euler_totient(n, table)
        length += 1
    return length + 1

result = 0
for i in range(len(primes_table)):
    if i % 10000 == 0:
        print(i)
    if chain_lenght(primes_table[i],fact_table) == 25:
        result += primes_table[i]

