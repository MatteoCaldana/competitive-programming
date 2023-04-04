# -*- coding: utf-8 -*-

res = 1
l = []

for i in range(1, 21):
    mult = i
    for j in l:
        if mult % j == 0:
            mult //= j
    l.append(mult)
    res *= mult
    
for i in range(1, 21):
    if res % i != 0:
        print(i)
        res = False
    

