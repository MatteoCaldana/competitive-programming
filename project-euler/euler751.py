# -*- coding: utf-8 -*-

NDIGITS = 100

def floor(x):
    return x // 10**NDIGITS 

def mantissa(x):
    return x % 10**NDIGITS

def B(b_old):
    return floor(b_old) * (mantissa(b_old) + 10**NDIGITS)

def tau(theta):
    b = [int(theta)]
    a = [floor(b[-1])]
    for i in range(2, NDIGITS-1): # each as at least 1 digit
        b.append(B(b[-1]))
        a.append(floor(b[-1]))
    #print(a)
    #print(b)
    return int(''.join([str(i) for i in a])[:NDIGITS+1])

theta = 2.956938891377988*10**NDIGITS
for i in range(100): # contraction? yes
    print(theta)
    theta = tau(theta)
    
    
    

    

