# -*- coding: utf-8 -*-

limit = 1001

table = []
for _ in range(limit):
    table.append(set())

def insert_and_expand_triple(triple, limit):
    global table 
    table[sum(triple)].add(triple)
    i = 2
    while sum(triple)*i < limit:
        table[sum(triple)*i].add(tuple([j*i for j in triple]))
        i += 1
    return


a, b, c = 0, 0, 0
n = 2
while a + b + c < limit:
    for m in range(1,n):
        a = n * n - m * m
        b = 2 * m * n
        c = m * m + n * n
        triple = (max(a,b), min(a,b), c)
        if sum(triple) < limit:
            insert_and_expand_triple(triple, limit)
    n += 1
    
res = [len(i) for i in table]