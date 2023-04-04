# -*- coding: utf-8 -*-

from utils import getdigits

def square_digit_chain(n):
    while n != 89 and n != 1:
        n = sum([i**2 for i in getdigits(n)])
    if n == 89:
        return 1
    return 0

result = 0
for i in range(2,10000000):
    if i % 100000 == 0:
        print(i)
    result += square_digit_chain(i)
    

    