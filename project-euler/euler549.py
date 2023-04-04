# -*- coding: utf-8 -*-

import random

def test(N, MOD):

    def gcd1(a, b):
        if b == 0:
            return a
        else:
            return gcd1(b, a % b)
    
    def gcd2(a, b):
        if b == 0:
            return a
        else:
            return gcd2(b, a % b % MOD)
    
    def G(N, gcd):
        res = 0
        for i in range(1, N+1):
            for j in range(1, i+1):
                res += gcd(i, j)
        return res % MOD
    
    g1 = G(N, gcd1)
    g2 = G(N, gcd2)
    print(g1, g2)
    assert(g1 == g2)
    
if __name__ == "__main__":
    for i in range(100):
        N = random.randint(3, 10**3)
        MOD = random.randint(3, N)
        print(N, MOD)
        test(N, MOD)
        print('-----------------------------')

    