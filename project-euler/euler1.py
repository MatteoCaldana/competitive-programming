# -*- coding: utf-8 -*-

res = []

for i in range(2, 1000):
    if (i % 3 == 0) or (i % 5 == 0):
        res.append(i)
        
res = sum(res)

