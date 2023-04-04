# -*- coding: utf-8 -*-

from itertools import permutations
from utils import getdigits, number_from_list

def check_ss_div(l):
    if(number_from_list(l[1:4]) % 2 == 0 and
       number_from_list(l[2:5]) % 3 == 0 and
       number_from_list(l[3:6]) % 5 == 0 and
       number_from_list(l[4:7]) % 7 == 0 and
       number_from_list(l[5:8]) % 11 == 0 and
       number_from_list(l[6:9]) % 13 == 0 and
       number_from_list(l[7:10]) % 17 == 0):
           return True
    return False

res = []
for i in permutations(list(range(10))):
    if check_ss_div(i):
       res.append(i) 
       
result = sum([number_from_list(i) for i in res])