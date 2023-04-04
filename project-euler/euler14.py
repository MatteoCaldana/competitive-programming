# -*- coding: utf-8 -*-

def collatz(l):
    n = l[-1]
    if n == 1:
        return l
    if n % 2 == 0:
        n //= 2
        l.append(n)
        collatz(l)
    else:
        n = 3*n + 1
        l.append(n)
        collatz(l)

l = 0

for i in range(1_000_000, 800_000, -1):
    tmp = [i]
    collatz(tmp)
    if i % 1000 == 0:
        print(i, l)
    tmpl = len(tmp)
    if tmpl > l:
        l = tmpl
        res = i

print(res)    

