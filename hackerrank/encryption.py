#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    r = int(len(s)**0.5)
    l = [(r,r),(r,r+1),(r+1,r+1)]
    l = [i for i in l if i[0]*i[1] >= len(s)]
    l = l[0]
    s = ''.join(s.split(' '))
    print(s)
    s = [s[i:len(s):l[1]] for i in range(l[1])]
    s = ' '.join(s)
    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
