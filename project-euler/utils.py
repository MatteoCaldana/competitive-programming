# -*- coding: utf-8 -*-

from bisect import bisect_left

def isprime(n):
    if n == 1:
        return False
    s = int( n**0.5 ) + 1
    for i in range(2, s):
        if n % i == 0:
            return False
    return True

def list_divisors(n):
    l = set([])
    s = int( n**0.5 + n/1e14 ) + 1
    for i in range(1,s):
        if n % i == 0:
            l.add(i)
            l.add(n//i)
    return list(l)

def fact(n):
    if n <= 1:
        return 1
    return n * fact(n - 1)
    
def getdigit(n,i):
    n = n % 10**i
    n = n // 10**(i-1)
    return n

def getndigits(n):
    n_digits = 0
    while (n // 10**n_digits) != 0:
        n_digits += 1
    return n_digits

def getdigits(n):
    res = []
    while (n // 10) != 0:
        res.append(n % 10)
        n = n // 10
    res.append(n)
    res.reverse()
    return res

def sum_digits(n):
   r = 0
   while n:
       r, n = r + n % 10, n // 10
   return r

def fib(n):
    if n <= 2:
        return 1
    prev, curr = (1, 1)
    for _ in range(n - 2):
        tmp = curr + prev
        prev = curr
        curr = tmp
    return curr

def gcd(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a

def rotate(l):
    res = []
    tmp = l
    for _ in range(len(l)-1):
        tmp = [tmp[-1]] + tmp[:-1]
        res.append(tmp)
    return res

def index(a, x):
    'Locate the leftmost value exactly equal to x'
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    return -1
    
def number_from_list(l):
    res = 0
    pw = 1
    for i in reversed(l):
        res += i * pw
        pw *= 10
    return res

#def fib(term, curr=1, prev=0):
#    if term == 0:
#        return prev
#    return fib(term - 1, prev + curr, curr)
    
def palindromiclist(l):
    for i in range(len(l) // 2):
        if l[i] != l[len(l)-i-1]:
            return False
    return True

def is_palindromic(n):
    return palindromiclist(getdigits(n))

def unit_frac_rep(den):
    n = len(str(den))
    rep = [0]*(n - 1)
    num = 10**(n - 1)
    seen_num = []
    compute_rep = True
    while compute_rep:
        rep.append(num // den)
        num = (num % den) * 10
        if num in seen_num:
            seen_num.append(num)
            compute_rep = False
        else:
            seen_num.append(num)
    return (rep, seen_num)