# -*- coding: utf-8 -*-

from utils import isprime, sum_digits

def isHarshad(n):
    if n % sum_digits(n) == 0:
        return True
    return False

def enhance_recursice_harshad(l, order):
    enhanced = []
    ll = len(l)
    for i in range(ll):
        h = l[i]
        for n in range(10**order):
            m = h*10**order + n
            tmp = True
            for i in range(order):
                tmp = tmp and isHarshad(m//(10**i))
            if tmp:
                enhanced.append(m)
    return enhanced

def isstrong(n):
    return isprime(n//sum_digits(n))

#harshad_recursive_1e6 = []
#
#print("fill 1e6 recursive harshad")
#for n in range(1_000_000,10_000_000):
#    if n % 100_000 == 0:
#        print(n)
#    if ( isHarshad(n) and isHarshad(n//10) and isHarshad(n//100) and 
#        isHarshad(n//1_000) and isHarshad(n//10_000) and isHarshad(n//100_000) ):
#        harshad_recursive_1e6.append(n)

#harshad_recursive_1e5 = []
#print("fill 1e5 recursive harshad")
#for n in range(100_000,1_000_000):
#    if ( isHarshad(n) and isHarshad(n//10) and isHarshad(n//100) and 
#        isHarshad(n//1_000) and isHarshad(n//10_000) ):
#        harshad_recursive_1e5.append(n)
#print(len(harshad_recursive_1e5))
#
#harshad_recursive_1e8 = []
#print("fill 1e8 recursive harshad")
#for h in harshad_recursive_1e5:
#    for n in range(0, 1_000):
#        m = h*1_000 + n
#        if isHarshad(m) and isHarshad(m//10) and isHarshad(m//100):
#            harshad_recursive_1e8.append(m)

h = [[i for i in range(1,10)]]

for i in range(12):
    print("enhance", i)
    h.append(enhance_recursice_harshad(h[i], 1))

print("find strong")
hh = []
for i in range(len(h)):
    for j in range(len(h[i])):
        if isstrong(h[i][j]):
            hh.append(h[i][j])

print("find prime")
hhh = []
for i in range(len(hh)):
    print(i, len(hh))
    for j in range(10):
        m = hh[i]*10+j
        if isprime(m):
            hhh.append(m)
            
for h in hhh:
    if (not isprime(h)) or (not isstrong(h//10)):
        print('AAAAAAAAAAAAAAAAAAAAA')

res = sum(hhh)

print(res)


