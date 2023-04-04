#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
    
def lcm(a, b):
    GCD = gcd(a, b)
    return a * b // GCD

def lcmArr(arr):
    if len(arr) == 1:
        return arr[0]
    LCM = lcm(arr[0], arr[1])
    for i in range(2, len(arr)):
        LCM = lcm(LCM, arr[i])
    return LCM

def gcdArr(arr):
    if len(arr) == 1:
        return arr[0]
    GCD = gcd(arr[0], arr[1])
    for i in range(2, len(arr)):
        GCD = gcd(GCD, arr[i])
    return GCD

def isInBetween(x, a, b):
    for aa in a:
        if x % aa != 0:
            return False
    for bb in b:
        if bb % x != 0:
            return False
    return True

def getTotalX2(a, b):
    # Write your code here
    LCMa = lcmArr(a)
    GCDb = gcdArr(b)
    if GCDb % LCMa != 0:
        return 0
    else:
        res = 0
        i = 1
        while LCMa <= GCDb:
            if GCDb % (LCMa * i) == 0:
                res += 1
            i += 1
        return res

def getTotalX(a, b):
    # Write your code here
    mmin = max(a)
    mmax = min(b)
    res = 0
    for i in range(mmin, mmax+1):
        if isInBetween(i, a, b):
            res += 1
    return res
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
