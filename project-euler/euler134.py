# -*- coding: utf-8 -*-
import time

def sieve(n):
    is_prime = [1]*n
    is_prime[0] = 0
    is_prime[1] = 0
    curr = 2
    while curr * curr < n:
        if is_prime[curr]:
            for i in range(curr * curr, n, curr):
                is_prime[i] = 0
        curr += 1
    return is_prime


def find_S(p1, p2, d):
    # the modular inverse `inv` is such that
    # (inv * p2) % d == 1
    # then
    # ((inv * p2) % d) * p1 == p1
    # so (recall p1 < d)
    # (inv * p2 * p1) % d == p1
    inv = pow(p2, -1, d)
    p = p2 * ((inv * p1) % d)
    return p

def find_S_naive(p1, p2, d):
    p = p2
    while p % d != p1:
        p += p2
    return p

t0 = time.time()
is_prime = sieve(2*10**6)
t1 = time.time()
primes = []
for i in range(len(is_prime)):
    if is_prime[i]:
        primes.append(i)
t2 = time.time()
print(t1 - t0, t2 - t1)

digits = [10]
for i in range(1, len(primes)):
    digits.append(digits[-1] * 10 ** (primes[i] // digits[i - 1] > 0))

Ss = []
i = 2
while primes[i] <= 10**6:
    if i % 100 == 0:
        print(i)
    S = find_S_naive(primes[i], primes[i + 1], digits[i])
    Ss.append(S)
    i += 1
result = sum(Ss)