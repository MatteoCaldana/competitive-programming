#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    is_am = -1
    if s[-2:] == 'AM':
        is_am = True
    else:
        is_am = False
    h = int(s[:2])
    if h == 12:
        if is_am:
            h = 0
    else:
        if not is_am:
            h += 12
    return '{:0>2}'.format(h)+s[2:-2]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
