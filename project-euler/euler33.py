# -*- coding: utf-8 -*-

from utils import getdigits, gcd
from functools import reduce 

possible_num_den = list(range(10,100))

res = []
for den_idx in range(len(possible_num_den)):
    den = possible_num_den[den_idx]
    for num_idx in range(den_idx):
        num = possible_num_den[num_idx]
        
        dig_den = getdigits(den)
        dig_num = getdigits(num)
        
        set_num = set(getdigits(den))
        set_den = set(getdigits(num))
        tmp = list(set_num & set_den)
        
        if len(tmp) == 1 and tmp[0]:
            dig_num.remove(tmp[0])
            dig_den.remove(tmp[0])
            
            if dig_den[0] != 0:
                original_float = num / den
                simplyfied_float = dig_num[0] / dig_den[0]
                if abs(original_float - simplyfied_float) < 1e-14:
                    res.append((num,den))
                    
                    
den = reduce(lambda x, y: x*y, [i[1] for i in res])
num = reduce(lambda x, y: x*y, [i[0] for i in res])
result = den // gcd(num,den)
            
        