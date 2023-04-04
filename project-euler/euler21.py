# -*- coding: utf-8 -*-

from utils import list_divisors

def list_p_div(n):
    l=list_divisors(n)
    l.remove(max(l))
    return l

def sum_p_div(n):
    return sum(list_p_div(n))

data = [i for i in range(5,10_001)]

for i in range(5,10_001):
    tmp = sum_p_div(i)
    print(i, tmp)
    if i != sum_p_div(tmp):
        data.remove(i)
    if i == tmp:
        data.remove(i)

res = sum(data)