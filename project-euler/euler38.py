# -*- coding: utf-8 -*-

# to have 9 digits and be greater that the example it is surely in 
res = []
for i in range(9183,10000):
    #print(i, i*2, i*100000+i*2)
    res.append(i*100000+i*2)
    
from utils import getdigits

result = [i for i in res if len(set(getdigits(i))) == 9]
# remove results with 0 digit