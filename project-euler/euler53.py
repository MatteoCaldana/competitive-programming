# -*- coding: utf-8 -*-

def bin_coef(n, k):
    res = 1
    m = max(n-k,k)
    for i in range(m+1,n+1):
        res *= i
    for i in range(1,n-m+1):
        res //= i
    return res

#print(bin_coef(100,4))

res = 0
for i in range(1,101):
    print(i)
    for j in range(3,max(4,i-3)):
        if bin_coef(i,j) > 1000000:
            res += 1
        
        