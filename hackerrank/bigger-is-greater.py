#!/bin/python3

import math
import os
import random
import re
import sys

def doable(w):
    for i in range(len(w)-1):
        if w[i] < w[i+1]:
            return True
    return False

# Complete the biggerIsGreater function below.
def biggerIsGreater(w):
    if not doable(w):
        return "no answer"

    idx = 0
    for i in range(len(w)-1):
        if w[i] < w[i+1]:
            idx = i
    tmp = w[idx+1:]
    tmp2 = [i for i in tmp if i > w[idx]]
    swap = min(tmp2)
    swap_idx = tmp.find(swap) + len(w) - len(tmp)
    to_reorder = w[idx+1:swap_idx] + w[idx] + w[swap_idx+1:]
    to_reorder = [c for c in to_reorder]
    to_reorder.sort()
    res = w[:idx] + swap + ''.join(to_reorder)
    return res
    



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
