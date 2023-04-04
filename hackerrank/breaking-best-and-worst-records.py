#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    mmin = scores[0]
    mmax = scores[0]
    mminc = 0
    mmaxc = 0
    for s in scores:
        if s < mmin:
            mmin = s
            mminc += 1
        elif s > mmax:
            mmax = s
            mmaxc += 1
    return [mmaxc, mminc]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
