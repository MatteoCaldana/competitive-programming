# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 17:12:47 2021

@author: matteo.caldana
"""

# speed ration = radius_1 / radius_n

# radius_n = (-1)^(n-1) sum _1 ^n (-1)^k distance_k + radius_1 

def check_valid(solution, distances):
    r = distances[0] - solution[0]/solution[1]
    for i in range(len(distances)-1):
        if r >= distances[i]:
            return [-1, -1]
        r = distances[i+1] - r
    if r >= distances[-1]:
        return [-1, -1]
    return solution

def solution(pegs):
    distances = []
    for i in range(len(pegs)-1):
        distances.append(pegs[i+1]-pegs[i])
    flip, flip_sum = 1, 0
    for d in distances:
        flip_sum += d * flip
        flip *= -1
    if flip_sum <= 0:
        return [-1, -1]
    if len(distances) % 2 == 0:
        return check_valid([2*flip_sum,1],distances)
    else:
        if flip_sum % 3== 0:
            return check_valid([2*(flip_sum//3),1],distances)
        else:
            return check_valid([2*flip_sum,3],distances)
        
print(solution([4, 17, 50]))