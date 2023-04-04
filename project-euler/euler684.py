# -*- coding: utf-8 -*-

#1    1    2      
#2    2    3      
#3    3    4      
#4    4    5      
#5    5    6      
#6    6    7      
#7    7    8      
#8    8    9      
#9    9    10      
#10   19   20      
#11   29   30      
#12   39   40      
#13   49   50      
#14   59   60      
#15   69   70      
#16   79   80      
#17   89   90      
#18   99   100      
#19   199  200      
#20   299  300
#       ->
#       +n (i.e. +1 each row)
#
#sum of 2nd column using the 3rd one
#sum_{i=0}^{m=1} {45 * 10^k} + sum_{i=1}^{p=3} {k * 10^(m+1)} - n - 1
#                 ^                                                 ^
#                 |                                                 |
#                 1 to 9 sum                                        start from 2
#
#m = n / 9 - 1
#p = n % 9 + 1

from utils import fib
from mod import Mod


def s(n):
    #tmp = [n%9]+[9]*(n//9)
    #return int(''.join([str(i) for i in tmp]))
    return 10**(n//9+1) - 1 - (10-n%9-1)*10**(n//9)

def S(k):
    return sum([s(i) for i in range(1,k+1)])

def S2(k):
    m = k // 9 - 1
    p = k % 9 + 1
    return sum([45 * 10**i for i in range(m+1)]) + sum([i * 10**(m+1) for i in range(1,p+1)]) - k - 1

def Smod(k):
    m = k // 9 - 1
    p = k % 9 + 1
        
    ###################################################
    # still tooo long
    tmp1 = 0
    for i in range(m+1):
        tmp1 = tmp1 + 45 * Mod(10,1000000007)**i
    ###################################################
    
    tmp2 = 0
    for i in range(1,p+1):
        tmp2 = tmp2 + i * Mod(10,1000000007)**(m+1)
                
    return tmp1 + tmp2 - k - 1

def Smod2(k):
    m = k // 9 - 1
    p = k % 9 + 1
    tmp1 = (Mod(10,1000000007)**(m+1)-1) / 9 # 111...1 = 999...9 / 9 = (10*n-1)/9
    return 45*tmp1 + sum([i * Mod(10,1000000007)**(m+1) for i in range(1,p+1)]) - k - 1


result = sum([Smod2(fib(i)) for i in range(2,91)])
