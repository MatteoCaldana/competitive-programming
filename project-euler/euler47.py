# -*- coding: utf-8 -*-

from factorize import fill_factorizations
import time

start_time = time.time()
table = fill_factorizations(1000000)
#for i in range(len(table)):
#    res = 1
#    for key in table[i]:
#        res*=key**table[i][key]
#    if res != i:
#        print("AAAAAAAAAAAAAAAAAA")
print("--- %s seconds ---" % (time.time() - start_time))

def check_n_consec_of_len_n_at_i(n, i):
    for j in range(n):
        if len(table[i+j]) != n:
            return False
    return True

def find_n_consec_of_len_n(n):
    for i in range(len(table)-n):
        if check_n_consec_of_len_n_at_i(n, i):
            return i
    return -1

result = find_n_consec_of_len_n(4)

