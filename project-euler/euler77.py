# -*- coding: utf-8 -*-

from factorize import fill_primes

primes = fill_primes(100000)

table_prime_sum = [set(),set()]

def prime_sums_count(n):
    global table_prime_sum
    for i in primes:
        if n < i:
            break
        elif n == i:
            table_prime_sum[n].add(tuple([i]))
        else:
            for j in table_prime_sum[n-i]:
                tmp = list(j) + [i]
                tmp.sort()
                table_prime_sum[n].add(tuple(tmp))
    return

for i in range(2,100):
    print(i)
    table_prime_sum.append(set())
    prime_sums_count(i)
