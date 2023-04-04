# -*- coding: utf-8 -*-

target = 600851475143

def isprime(n):
    s = int( n**0.5 ) + 1
    for i in range(2, s):
        if n % i == 0:
            return False
    return True
   
for i in range(2, target):
    if target % i == 0:
        tmp = target//i
        print(i, tmp)
        if isprime(tmp):
            res = tmp
            break
