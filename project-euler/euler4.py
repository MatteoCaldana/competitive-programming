# -*- coding: utf-8 -*-

n = 1000**2

def getdigit(n,i):
    n = n % 10**i
    n = n // 10**(i-1)
    return n

def ispalindromic(n):
    n_digits = 0
    while (n // 10**n_digits) != 0:
        n_digits += 1
    
    for i in range(1, n_digits//2 + 1):
        if getdigit(n, i) != getdigit(n, n_digits-i+1):
            return False
    return True

for i in range(n):
    m = n-i
    if ispalindromic(m):
        for j in range(100,999):
            k = 999-j+100
            if m % k == 0:
                d = m//k
                if d // 100 != 0 and d // 1000 == 0:
                    print(d,k,m)
                    break

