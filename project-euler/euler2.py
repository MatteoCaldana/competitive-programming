# -*- coding: utf-8 -*-

fib1 = 1
fib2 = 1
l = []

while fib2 < 4_000_000:
    if fib2 % 2 == 0:
        l.append(fib2)
    tmp = fib2 + fib1
    fib1 = fib2
    fib2 = tmp

res = sum(l)
    

