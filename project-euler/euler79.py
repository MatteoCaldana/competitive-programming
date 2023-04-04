# -*- coding: utf-8 -*-

with open("p079_keylog.txt",'r') as f:
    data = f.read()
    
data = data.split('\n')
data = [[int(j) for j in i] for i in data[:-1]]

after_before = []
for i in range(10):
    after_before.append((set(),set()))
    
for passcode in data:
    after_before[passcode[0]][0].add(passcode[1])
    after_before[passcode[0]][0].add(passcode[2])
    
    after_before[passcode[1]][0].add(passcode[2])
    after_before[passcode[1]][1].add(passcode[0])
    
    after_before[passcode[2]][1].add(passcode[0])
    after_before[passcode[2]][1].add(passcode[1])
    

for i in range(len(after_before)):
    after_before[i] = (list(after_before[i][0]),list(after_before[i][1]))

def find_trivial_next(after_before):
    res = []
    for i in range(len(after_before)):
        if len(after_before[i][1]) == 0 and len(after_before[i][0]) != 0:
            res.append(i)
    return res

def update_before(after_before, n):
    for i in range(len(after_before)):
        if n in after_before[i][1]:
            after_before[i][1].remove(n)
    return

def empty(after_before):
    for i in range(len(after_before)): 
        if len(after_before[i][1]) > 0:
            return False
    return True

def solve(after_before):
    sol = []
    while not empty(after_before):
        ns = find_trivial_next(after_before)
        tmp = list(set(ns)-set(sol))
        if len(tmp) != 1:
            raise ValueError("Non-trivial solution")
        sol.append(tmp[0])
        update_before(after_before, tmp[0])
    return sol
    

    
    
    