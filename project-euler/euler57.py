# -*- coding: utf-8 -*-

from utils import gcd
from fraction import Fraction

def one_iter(t):
    return 1 + 1/(1 + t)

result = 0
a = Fraction(3,2)
for i in range(1000):
    a = one_iter(a)
    n, d = a.numden()
    if len(str(n)) > len(str(d)):
        result += 1    















