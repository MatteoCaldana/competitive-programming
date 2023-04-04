#!/bin/python3

import math
import os
import random
import re
import sys

def flip(b):
    if b:
        return 0
    return 1

# Complete the flippingBits function below.
def flippingBits(n):
    bits = list("{0:b}".format(n))
    bits = ['0']*(32-len(bits)) + bits
    bits = [flip(int(b)) for b in bits]
    res = 0
    for i in range(32):
        res += bits[31-i]*2**i
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
