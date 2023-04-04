# -*- coding: utf-8 -*-

def couples_that_sum_to(n):
    l = []
    for i in range(1, n//2 + 1):
        l.append([i,n-i])
    return l

for c in range(998,0,-1):
    l = couples_that_sum_to(1000 - c)
    for [a, b] in l:
        if a**2 + b**2 == c**2:
            print(a,b,c)
            break
    else:
        continue
    break

res = a*b*c

