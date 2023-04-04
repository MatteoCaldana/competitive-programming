# -*- coding: utf-8 -*-

from mod import Mod

def hyperexp(a,k):
    index = k.n
    result = a
    while index > 1:
        result = a**(result.n)
        index -= 1
    return result


a = hyperexp(Mod(1777,10**8),Mod(1855,10**8))