# -*- coding: utf-8 -*-

from utils import getdigit

base_cases = {
        0: '',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen'
        }

ty_cases = {
        2: 'twenty',
        3: 'thirty',
        4: 'forty',
        5: 'fifthy',
        6: 'sixty',
        7: 'seventy',
        8: 'eighty',
        9: 'ninty'
        }

def write_number(n):
    if n < 20:
        return base_cases[n]
    if n < 100:
        return ty_cases[getdigit(n,2)]+base_cases[getdigit(n,1)]
    if n < 1000:
        add = write_number(n%100)
        add = 'and'+add if add != '' else add
        return base_cases[getdigit(n,3)]+'hundred'+add
    if n == 1000:
        return 'onethousand'
    
res = ''
for i in range(1,1001):
    res += write_number(i)
        

