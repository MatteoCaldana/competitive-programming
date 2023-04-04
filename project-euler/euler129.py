# -*- coding: utf-8 -*-

from mod import Mod
import time

def R(k, mod):
    if mod % 3 == 0:
        return R3(k, mod)
    return (Mod(10,mod)**k - 1) / Mod(9,mod)

# for when mod % 3 == 0
# compute R in log time
# compute summing the powers of ten 1 -> 11 -> 1111 -> 11111111 -> ...
# exploit the binary representation of k like in the log exponientiation
def R3(k, mod):
    result = Mod(0,mod)
    result_digits = 0
    curr_result = Mod(1,mod)
    curr_result_digits = 1
    byte = 1
    byteshift = k
    while byteshift:
        if k & byte:
            result = result + curr_result * Mod(10,mod)**result_digits
            result_digits += curr_result_digits
                        
        byte *= 2
        byteshift >>= 1
            
        curr_result = curr_result + curr_result * Mod(10,mod)**curr_result_digits
        curr_result_digits *= 2
    return result
    

def Rtest(k):
    return (10**k - 1)//9

def A(n):
    for i in range(10**6,10**7):
        if R(i,n).n == 0:
            return i
        
#for i in range(10000):
#    if R3(i,0) != Rtest(i):
#        print(i)
#        break
            
#start_time = time.time()
#for i in range(30000):
#    a = R3(i,9)
#print("--- %s seconds ---" % (time.time() - start_time))
        
#for i in range(5,10**8,2):
#    if i % 3**5 == 0:
#        print(i)
#    if i % 5 != 0:
#        if A(i) > 10**6:
#            result = i
#            print(i, A(i))
#            break