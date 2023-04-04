# -*- coding: utf-8 -*-

from utils import getdigits, number_from_list, is_palindromic
import time

def isPalindrome(n):
    return str(n)[::-1] == str(n)[:]

def isLychrel(n, remaining_iter=55):
    if remaining_iter == 0:
        return True
    n = int(str(n)[::-1]) + n
    if isPalindrome(n):
        return False
    return isLychrel(n, remaining_iter - 1)

#print(isLychrel(10677))
    
start_time = time.time()  
result = 0
for i in range(10000):
    if isLychrel(i):
        result += 1
print("--- %s seconds ---" % (time.time() - start_time))
