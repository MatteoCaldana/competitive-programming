# -*- coding: utf-8 -*-

from fraction import Fraction

current = Fraction(0)
objective = Fraction(3,7)
float_obj = objective.approx()

for i in range(2, int(1e6)+1):    
    heuristic = int(float_obj*i)
    for j in range(heuristic, heuristic+2):
        tmp = Fraction(j,i)
        if current < tmp and tmp < objective: 
            current = tmp
            
print(current)