# -*- coding: utf-8 -*-

def isprime(n):
    s = int( n**0.5 ) + 1
    for i in range(2, s):
        if n % i == 0:
            return False
    return True

n_primes = 0
n = 2

while n_primes < 10_001:
    print(n)
    if isprime(n):
        n_primes += 1
    n += 1
    
res = n
    

