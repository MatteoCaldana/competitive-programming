#!/bin/python3

import math
import os
import random
import re
import sys

def count(l):
    res = [0]*(max(l)+1)
    for i in range(len(l)):
        res[l[i]] += 1
    return res

# Complete the missingNumbers function below.
def missingNumbers(arr, brr):
    count_arr = count(arr)
    count_brr = count(brr)
    count_arr += [0]*(len(count_brr)-len(count_arr))

    res = []
    for i in range(len(count_arr)):
        if count_brr[i] != count_arr[i]:
            res.append(i)
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    m = int(input())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
