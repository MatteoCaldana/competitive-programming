# -*- coding: utf-8 -*-

#               1!/0!1!   1!/1!0!
#
#          2!/0!2!   2!/1!1!   2!/2!0!
#
#     3!/0!3!   3!/1!2!   3!/2!1!   3!/3!0!
#
#4!/0!4!   4!/1!3!   4!/2!2!   4!/3!1!   4!/4!0! #
#     ^         ^                 ^         ^
#     n + 1     n!                n!        n + 1        

# Notice that between row n and (n + 1) at the numerator we add n factors 
# (n + 1) and we add one (n + 1)!, meanwhile at the denominator we add 2 factors 
# (n + 1) and we add two n!, indeed for ex. at the denominator we use the two 2! 
# and the two 1! from layer 3 in the layer 4
# Thus we have (n + 1)**n * (n + 1)! / (n + 1)**2 (n!)**2
# = (n + 1)**(n - 1) * (n + 1) / n! 
# = (n + 1)**n / n!
# = m**(m - 1) / (m - 1)! #(m = n + 1)

# https://en.wikipedia.org/wiki/Divisor_function
# n = p_1**a_1 * ... * p_r**a_r
# sum divisors = product_{i=1}^{number of distinct prime factors} (p_i**(a_i+1)-1)/(p_i-1)

from factorize import fill_factorizations
from operator import add
from mod import Mod
import time

fact_table = fill_factorizations(20001)

# list version
#def factorize_factorial(n,fact_table,factorial_fact_table):
#    result = factorial_fact_table[n-1].copy()
#    fact_n = fact_table[n] 
#    # add factors n
#    for i in fact_n:
#        result[i] += fact_n[i]
#    factorial_fact_table.append(result)
#    return factorial_fact_table
#
#def fill_factorize_factorial_table(limit, fact_table):
#    table = [[0,1]+[0]*limit]
#    for i in range(1,limit):
#        table = factorize_factorial(i,fact_table,table)
#    return table

def factorize_factorial(n,fact_table,factorial_fact_table):
    result = factorial_fact_table[n-1].copy()
    fact_n = fact_table[n]
    # add factors n
    for i in fact_n:
        if i in result:
            result[i] += fact_n[i]
        else:
            result[i] = fact_n[i]
    factorial_fact_table.append(result)
    return factorial_fact_table

def fill_factorize_factorial_table(limit, fact_table):
    table = [{}]
    for i in range(1,limit):
        table = factorize_factorial(i,fact_table,table)
    return table
    
def factorize_B(n, fact_table, factorial_fact_table, B_table):
    result = B_table[n-1].copy()
    denominator = factorial_fact_table[n-1].copy()
    numerator = fact_table[n].copy()
    numerator.update((x, y*(n-1)) for x, y in numerator.items())
    for i in numerator:
        if i in result:
            result[i] += numerator[i]
        else:
            result[i] = numerator[i]
    for i in denominator:
        result[i] -= denominator[i]
    B_table.append(result)
    return B_table

def fill_B_table(limit, fact_table, factorial_fact_table):
    table = [{}]
    for i in range(1,limit):
        table = factorize_B(i,fact_table,factorial_fact_table,table)
    return table

def sum_divisors(factorization):
    #https://en.wikipedia.org/wiki/Divisor_function, see comment at top of this file
    mod = 10**9+7
    result_mod = Mod(1,mod)
    #result = 1
    for i in factorization:
        result_mod = result_mod * (Mod(i,mod)**(factorization[i]+1) - 1)
        #result *= i**(factorization[i]+1) - 1
                
    for i in factorization:
        # mod is prime, then 
        # a**-1 == a**(mod-2), i.e.
        # result_mod / Mod((i - 1),mod) == result_mod * Mod((i - 1),mod)**(mod-2)
        result_mod = result_mod / Mod((i - 1),mod)
        #result //= i - 1
        
    return result_mod

def S(n, B_table):
    result = 0
    for i in range(1,n+1):
        if i % 10 == 0:
            print(i)
        result = result + sum_divisors(B_table[i])
    return result
    

start_time = time.time()
# map is faster
limit = 20000
factorial_fact_table = fill_factorize_factorial_table(limit+1,fact_table)
B_table = fill_B_table(limit+1,fact_table,factorial_fact_table)
for i in range(1,len(B_table)):
    del(B_table[i][1])
result = S(limit,B_table)
print("--- %s seconds ---" % (time.time() - start_time))
    

###############################################################################
#                              OLD                                            #
###############################################################################

def gen_divisors_from_factorization(factorization):
    base = [i for i in range(len(factorization)) if factorization[i] != 0]
    exp = [factorization[i] for i in range(len(factorization)) if factorization[i] != 0]
    
    divisors_exp, tmp_enhance = [[]], []
    
    # if n = p_1**k_1 * ... * p_m**k_m
    # all divisors are of the form p_1**K_1 * ... * p_m**K_m
    # where K_i \in [0,k_i]
    # dynamic programming to generate all the possible exponentials of the divisors
    for fact in exp:
        for i in range(fact+1):
            for partial_exp in divisors_exp:
                tmp_enhance.append(partial_exp+[i])
        divisors_exp, tmp_enhance = tmp_enhance, []
                
    divisors = [gen_number_from_factorization(exp, base) for exp in divisors_exp]
    
    return divisors

#a=gen_divisors_from_factorization(factorize_B(5,fact_table))


















