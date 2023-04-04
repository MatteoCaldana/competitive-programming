#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    zer = 0
    pos = 0
    neg = 0
    for x in arr:
        if x == 0:
            zer += 1
        elif x > 0:
            pos += 1
        else:
            neg += 1
    L = len(arr)
    def printf(f):
        print('{:.6f}'.format(f))
    
    printf(pos/L)
    printf(neg/L)
    printf(zer/L)
    return

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
