# -*- coding: utf-8 -*-

def generate(n_gens):
    old_gen = [(2, 1)]
    new_gen = []
    for i in range(n_gens):
        for g in old_gen:
            new_gen.append((g[0]+g[1],g[0]))
            new_gen.append((g[0]+g[1],g[1]))
        old_gen = new_gen
        new_gen = []
    old_gen.sort(key=lambda x: x[1]/x[0])
    print('gen', i, old_gen[:50])
        
def fib(n):
    fib = [1, 1]
    for i in range(n):
        fib.append(fib[-1]+fib[-2])
    return fib

#fib = fib(239)
        
def rec_solution(x,y):
    if x < y:
        X, Y = y, x
    else:
        X, Y = x, y
    if (X - Y == 1) or Y == 1:
        return X - 1
    if X % Y == 0:
        return -10**50
    else:
        n = X // Y
        return n + rec_solution(X%Y,Y)

def solution(x, y):
    X = int(x)
    Y = int(y)
    sol = rec_solution(X,Y) #'impossible'
    if sol > 0:
        return sol
    else:
        return 'impossible'
