# -*- coding: utf-8 -*-

from utils import getdigits

def count_dig(l):
    res = [0]*10
    for i in range(len(l)):
        res[l[i]] += 1
    return res

def same_dig(n1, n2):
    l1 = count_dig(getdigits(n1))
    l2 = count_dig(getdigits(n2))
    for i in range(len(l1)):
        if l1[i] != l2[i]:
            return False
    return True

n_dig = 5
res = []
for i in range(10**n_dig, 10**(n_dig+1)//6):
    if same_dig(i, 2*i):
        res.append(i)

res2 = []
for i in res:
    if same_dig(i, 3*i):
        res2.append(i)     
        
res3 = []
for i in res2:
    if same_dig(i, 4*i):
        res3.append(i)
        
res4 = []
for i in res3:
    if same_dig(i, 5*i):
        res4.append(i)
        
result = []
for i in res4:
    if same_dig(i, 6*i):
        result.append(i) 
        
        
        
        