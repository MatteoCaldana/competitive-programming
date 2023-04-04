# -*- coding: utf-8 -*-

from utils import index
import time

def ispentagonal(n):
    return (1 + 24 * n)**0.5 % 6 == 5

start_time = time.time()

for j in range(1,5000):
    pj = j * (3 * j - 1) // 2
    for k in range(j+1, 5000):
        pk = k * (3 * k - 1) // 2
        if ispentagonal(pk-pj) and ispentagonal(pk+pj):
            print(k, j, pk, pj, pk-pj)
            
print("--- %s seconds ---" % (time.time() - start_time))
        
 ############################################################################

start_time = time.time()

limit = 5000 # max pentagonal generated
pentagonals = []
for i in range(1,limit):
    pentagonals.append(i*(3*i-1)//2)
    
def ispentagonal(n):
    global pentagonals
    return index(pentagonals, n) != -1

for i in range(len(pentagonals)):
    for j in range(i):
        if ispentagonal(pentagonals[i]-pentagonals[j]) and ispentagonal(pentagonals[i]+pentagonals[j]):
            print(i, j, pentagonals[i], pentagonals[j])
            
print("--- %s seconds ---" % (time.time() - start_time))






