#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    mmin = 10**10
    mmax = -10**10
    ssum = 0
    for x in arr:
        if x < mmin:
            mmin = x
        if x > mmax:
            mmax = x
        ssum += x
    print(ssum - mmax, ssum - mmin)
    return 

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
