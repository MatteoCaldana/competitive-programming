#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the balancedSums function below.
def balancedSums(arr):
    checked_indexes = set()
    old_idx = -1
    idx = len(arr) // 2
    ub = len(arr)
    lb = 0
    change = True
    while change:
        s_lx = sum(arr[:idx])
        s_rx = sum(arr[idx+1:])
        if s_lx == s_rx:
            return "YES"
        checked_indexes.add(idx)
        if s_lx > s_rx:
            ub = idx
        else:
            lb = idx
        old_idx = idx
        idx = (ub + lb) // 2

        if idx == old_idx:
            change = False
    
    for i in range(max(idx-1,0),min(idx+1,len(arr))):
        s_lx = sum(arr[:i])
        s_rx = sum(arr[i+1:])
        if s_lx == s_rx:
            return "YES"

    return "NO"



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(result + '\n')

    fptr.close()
