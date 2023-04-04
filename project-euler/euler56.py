# -*- coding: utf-8 -*-

from utils import getdigits
import numpy as np
import time

digit_sum_limit = 1000000
digit_sum_table = np.array([0,1,2,3,4,5,6,7,8,9]+[0]*(digit_sum_limit-10))
for i in range(10, digit_sum_limit):
    digit_sum_table[i] = digit_sum_table[i//10] + i%10
    
def digit_sum(n):
    if n < digit_sum_limit:
        return digit_sum_table[n]
    return n%10 + digit_sum(n//10)

def digit_sum2(n):
    return sum(getdigits(n))

start_time = time.time()
result = 0
for a in range(1,100):
    for b in range(1,100):
       tmp = digit_sum2(a**b)
       if tmp > result:
           print(a,b,a**b)
           result = tmp
print("--- %s seconds ---" % (time.time() - start_time))
