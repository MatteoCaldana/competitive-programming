#!/bin/python3

import math
import os
import random
import re
import sys

def check_cavity(grid, i, j):
    tmp = grid[i][j]
    return (grid[i+1][j] < tmp and 
            grid[i-1][j] < tmp and 
            grid[i][j+1] < tmp and 
            grid[i][j-1] < tmp)

# Complete the cavityMap function below.
def cavityMap(grid):
    result = []
    for i in range(1, len(grid)-1):
        for j in range(1, len(grid[i])-1):
            if check_cavity(grid, i, j):
                result.append((i,j))
                
    for i in result:
        tmp = list(grid[i[0]])
        tmp[i[1]] = 'X'
        grid[i[0]] = ''.join(tmp)
    return grid

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
