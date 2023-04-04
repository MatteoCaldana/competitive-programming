# -*- coding: utf-8 -*-

from utils import fact

n = 10**12

i = 1
res = 0
while 5**i < n:
    res += n // (5**i)
    i += 1
    
def fact5(n):
    i = 0
    while n % 5**i == 0:
        i += 1
    return i - 1
    
res = 1
for i in range(1, n):
    if i % 1000000 == 0:
        print(i)
    #i //= 5**fact5(i)
    res *= i
    res %= 1000000
    
        