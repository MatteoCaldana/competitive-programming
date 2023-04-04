# -*- coding: utf-8 -*-

import numpy as np

with open("p081_matrix.txt",'r') as f:
    data = f.read()
    
data = data.split('\n')[:-1]
data = np.array([[int(j) for j in i.split(',')] for i in data])

infty = sum(sum(data)) + 1

def dijkstra(matrix):
    dist = infty*np.ones((matrix.shape[0]*matrix.shape[1],)).astype(int)
    dist[0] = matrix[0,0]
    
    prev = -1*np.ones((matrix.shape[0]*matrix.shape[1],)).astype(int)
    
    to_visit = dist.copy()
    
    count = 0
    while prev[-1] == -1:
        index = np.argmin(to_visit)
        to_visit[index] = infty + 1
        i, j = index // matrix.shape[0], index % matrix.shape[1]
        
#        print(i,j)
#        print(dist)
#        print(prev)
#        print(to_visit)
#        print("================================================")
        
        for k, l in [(i+1,j), (i,j+1)]:
            if k < matrix.shape[0] and l < matrix.shape[1]:
                curr_dist = dist[index] + matrix[k,l]
                curr_index = k*matrix.shape[0] + l
                if curr_dist < dist[curr_index]:
                    dist[curr_index] = curr_dist
                    prev[curr_index] = index
                    
                    to_visit[curr_index] = curr_dist
    
        count += 1

                    
    return dist, prev

def recover_path(prev):
    res = [prev[-1]]
    while res[-1] != -1:
        res.append(prev[res[-1]])
    return res

test = [[131,  673,  234,  103,  18 ],
        [201,  96 ,  342,  965,  150],
        [630,  803,  746,  422,  111],
        [537,  699,  497,  121,  956],
        [805,  732,  524,  37 ,  331]]

a, b = dijkstra(np.array(data))

res = recover_path(b)

result = a[-1]






















