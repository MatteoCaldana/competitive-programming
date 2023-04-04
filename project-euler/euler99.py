# -*- coding: utf-8 -*-

from math import log

with open("p099_base_exp.txt",'r') as f:
    data = f.read()
    
data = data.split('\n')

def estimate(line):
    n = [int(i) for i in line.split(',')]
    return log(n[0])*n[1]

res = [] 
for i in data:
    res.append(estimate(i))
    
print(res.index(max(res))+1)