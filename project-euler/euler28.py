# -*- coding: utf-8 -*-

import operator
import numpy as np

directions = [(0,1), (1,0), (0,-1), (-1,0)]

n = 1001

a = np.ones((n,n),dtype=int)

def spiral(init, max_num):
    global a
    num = 1
    curr = init
    edge_dim = 1
    edge_num = 0
    while True:
        for _ in range(2):
            for i in range(edge_dim):
                curr = tuple(map(operator.add, curr, directions[edge_num % 4]))
                num += 1
                if num > max_num:
                    return
                a[curr] = num
            edge_num += 1
        edge_dim += 1

spiral((n//2,n//2),n**2)

result = -1
for i in range(n):
    result += a[0+i,0+i]
    result += a[n-i-1,i]

