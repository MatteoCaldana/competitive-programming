# -*- coding: utf-8 -*-

from utils import index

pentas = []
hexas = []
triangs = []

limit = 100000

for i in range(142,limit):
    hexas.append(i*(2*i-1))
    
for i in range(164,limit):
    pentas.append(i*(3*i-1)//2)
    
for i in range(284,limit):
    triangs.append(i*(i+1)//2)

res_pentas = []
for i in triangs:
    idx = index(pentas, i)
    if idx != -1:
        res_pentas.append(idx)
      
res_hexas = []
for i in res_pentas:
    idx = index(hexas, pentas[i])
    if idx != -1:
        res_hexas.append((idx, i)) 
        
result = hexas[res_hexas[-1][0]]
check_result = pentas[res_hexas[-1][1]]