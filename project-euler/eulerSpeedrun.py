# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 21:21:11 2021

@author: Matteo
"""

import time
import math

def euler1():
    return sum([i for i in range(1000) if (i % 3 == 0) or (i % 5 == 0)])

def euler2():
    res = 0
    fib1 = 1
    fib2 = 1
    while fib1 <= 4*10**6:
        tmp = fib1
        fib1 += fib2
        fib2 = tmp
        res += fib1 * (fib1 % 2 == 0)
    return res

def sieve(n):
    prime = [True]*(n+1)
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p*p, n+1, p):
                prime[i] = False
        p += 1
    return prime

def euler3():
    N = 600851475143
    primes = sieve(int(N**0.5))
    for i in range(len(primes)):
        if primes[len(primes)-i-1] and N % i == 0:
            return i
    
def is_palindrome(n):
    s = str(n)
    return s == s[::-1]
    
def euler4():
    N = 1000
    lb = N // 10 - 1
    res = 0
    for i in range(N-1, lb, -1):
        for j in range(i, lb, -1):
            if is_palindrome(i*j):
                # once we find one palindrome we check for only i*j that could be bigger
                lb = max(lb, i*j // N + 1)
                # store the largest
                res = max(res, i*j)
    return res
            
def euler5():
    N = 20
    fact = list(range(1, N+1))
    res = 1
    for i in range(N):
        res *= fact[i]
        for j in range(i+1, N):
            fact[j] = fact[j] if fact[j] % fact[i] else fact[j] // fact[i]
    return res

def euler6():
    square_of_sum = lambda n: (n*(n+1)//2)**2
    sum_of_square = lambda n: n*(n+1)*(2*n+1) // 6
    return square_of_sum(100) - sum_of_square(100)

def euler7():
    N = 10001
    primes = sieve(int(N*math.log(N))*10)
    count = 0
    for i in range(2, len(primes)):
        if primes[i]:
            count += 1
        if count == N:
            return i

def euler8():
    digits = """73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450"""
    WINDOW = 13
    digits = [s for s in digits.replace('\n','').split('0') if len(s) >= WINDOW]
    def brute_force(s):
        res = 0
        for i in range(len(s) - WINDOW):
            tmp = 1
            for j in range(WINDOW):
                tmp *= int(s[i+j])
            res = max(res, tmp)
        return res
    return max([brute_force(x) for x in digits])

def euler9():
    N = 1000
    for b in range(1, N//2):
        num = ( N**2 - 2 * N * b + 2 * b**2 )
        den = 2 * ( N - b )
        if num % den == 0:
            c = num // den
            a = N - b - c
            if a**2 + b**2 == c**2 and a + b + c == N:
                return a*b*c

def euler10():
    N = 2*10**6
    primes = sieve(N)
    res = 0
    for i in range(N):
        res += primes[i] * i
    return res

def euler12():
    N = 500
    triangular = lambda x: x*(x+1)//2
    def num_divisors(n):
        res = 2
        for i in range(2, int(n**0.5) + 1):
            res += 2 * (n % i == 0) 
        return res
    triangular = 1
    n_div = 1
    i = 2
    while n_div < 501:
        triangular += i
        i += 1
        n_div = num_divisors(triangular)
    return triangular


if __name__ == "__main__":
    start_time = time.time()
    print(euler12())
    print("--- %s seconds ---" % (time.time() - start_time))