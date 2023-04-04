# -*- coding: utf-8 -*-

from factorize import fill_factorizations

table = fill_factorizations(20000001)

def factorize_bin_coef(n,k,fact_table):
    m = max(k,n-k)
    result = {}
    
    # add factors of numerator
    for i in range(m+1,n+1):
        for j in fact_table[i]:
            if j in result:
                result[j] += fact_table[i][j]
            else:
                result[j] = fact_table[i][j]
    # subtract factors of denominator
    for i in range(2,n-m+1):
        for j in fact_table[i]:
            result[j] -= fact_table[i][j] 
    return result

fact_bin_coef = factorize_bin_coef(20000000,15000000,table)

result = 0
for i in fact_bin_coef:
    result += fact_bin_coef[i]*i
print(result)