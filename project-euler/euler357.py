# -*- coding: utf-8 -*-

# 2019

#from factorize import fill_primes
#
#l = []
#for i in range(2,10**8,4):
#    if isprime(i + 2):
#        l.append(i)
#        print(i)
        
###############################################################################

from factorize import fill_primes
import time

start_time = time.time()
table= fill_primes(10**7)
print("--- %s seconds ---" % (time.time() - start_time))


