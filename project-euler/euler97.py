# -*- coding: utf-8 -*-


e = 7830457

res = 1
for i in range(e):
    res *= 2
    res %= 10**11
    
res *= 28433
res += 1
