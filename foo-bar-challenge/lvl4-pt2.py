# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 08:58:14 2021

@author: matteo.caldana
"""
import operator
import functools
import random
import time

def build_primes_to(n):
    result = [2, 3, 5, 7]
    for i in range(result[-1]+1, n+1):
        if check_prime(i, result):
            result.append(i)
    return result
    
def check_prime(n, table):
    max_check = int(n**0.5) # since n small is a safe operation
    i = 0
    while table[i] <= max_check:
        if n % table[i] == 0:
            return False
        i += 1
    return True
    
def build_factorization_to(n):
    primes = build_primes_to(n)
    result = [{},{1:1},{2:1},{3:1},{2:2}]
    for i in range(len(result),n+1):
        result.append(get_factorization(i, primes, result))
    return primes, result
    
def get_factorization(n, primes, table):
    if n in primes: #TODO: explot primes is sorted
        return {n:1}
    for p in primes:
        if n % p == 0:
            divisor_factorization = table[n//p].copy()
            if p in divisor_factorization:
                divisor_factorization[p] += 1
            else:
                divisor_factorization[p] = 1
            return divisor_factorization
            
def get_directions(position, x_dim, y_dim, f):
    result = set()
    for i in range(1, x_dim+1):
        for j in range(1, y_dim+1):
            direction = make_prime(i - position[0], j - position[1], f)
            result.add(direction)
    return result

    
def make_prime(num, den, f):
    g = gcd(num, den)
    return (num//g, den//g)
        
##############################################################################

def get_pos(xy, xyc, dim, ij):
    if ij % 2 == 0:
        return ij*dim + xy
    else:
        return xy + (ij-1)*dim + 2*xyc

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def sign(x):
    if x < 0:
        return -1
    return 1

def reduced_fraction(a,b):
    sa, sb = sign(a), sign(b)
    if a == 0:
        return 0, sb
    if b == 0:
        return sa, 0
    GCD = gcd(sa*a,sb*b)
    return a//GCD, b//GCD
      
def build_positions(dimensions, your_position, trainer_position, distance):
    D2 = distance*distance
    your_ps = {}
    trai_ps = {}
    x_dim, y_dim = dimensions
    xyp, yyp = your_position
    xypc, yypc = x_dim - xyp, y_dim - yyp
    xtp, ytp = trainer_position
    xtpc, ytpc = x_dim - xtp, y_dim - ytp
    max_k = (distance // x_dim) + 1
    max_l = (distance // y_dim) + 1
    for i in range(-max_k,max_k+1):
        for j in range(-max_l,max_l+1):
            def put_in_table(xp, yp, xcp, ycp, table):
                x, y = get_pos(xp, xcp, x_dim, i), get_pos(yp, ycp, y_dim, j)
                d2 = (yyp-y)*(yyp-y)+(xyp-x)*(xyp-x)
                if d2 <= D2:
                    bearing = reduced_fraction(x-xyp, y-yyp)
                    if not ((bearing in table) and table[bearing][1] <= d2):
                        table[bearing] = ((x,y),d2)
            
            put_in_table(xyp, yyp, xypc, yypc, your_ps)
            put_in_table(xtp, ytp, xtpc, ytpc, trai_ps)
    return your_ps, trai_ps

def bisect_left(a, x):
    lo = 0
    hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if a[mid][0] < x: lo = mid+1
        else: hi = mid
    return lo

def check_self_shoot(yps, tp, p0):
    idx = bisect_left(yps, tp[0])
    if idx < len(yps) and yps[idx][0] == tp[0] and in_range(yps[idx][1], p0, tp[1]):
        return True
    return False

def in_range(t, t0, t1):
    return t[0] <= max(t0[0],t1[0]) and t[0] >= min(t0[0],t1[0]) and t[1] <= max(t0[1],t1[1]) and t[1] >= min(t0[1],t1[1])
    
def check_possible(yps, tps, p0):
    count = 0
    for tp in tps:
        if not check_self_shoot(yps, tp, p0):
            count += 1
    return count



test1 = {"dimensions":[3,2], "your_position":[1,1], "trainer_position":[2,1], "distance":4}
test2 = {"dimensions":[300,275], "your_position":[150,150], "trainer_position":[185,100], "distance":500}

test = test1

def solution(dimensions, your_position, trainer_position, distance):
    start_time = time.time()
    yps, tps = build_positions(dimensions, your_position, trainer_position, distance)
    print('--', time.time() - start_time)
    
    start_time = time.time()
    yps = [(k,yps[k][0]) for k in yps]
    yps.sort(key=lambda x: x[0])
    tps = [(k,tps[k][0]) for k in tps]
    tps.sort(key=lambda x: x[0])
    print('--', time.time() - start_time)
    
    return check_possible(yps, tps, your_position)
    
#print(solution(**test))



def make_test():
    dimension = [random.randint(2,1250) for i in range(2)]
    your_position = [random.randint(1,dimension[i]-1) for i in range(2)]
    trainer_position = [random.randint(1,dimension[i]-1) for i in range(2)]
    distance = random.randint(1,10**4)
    return {"dimensions":dimension, "your_position":your_position, "trainer_position":trainer_position, "distance":distance}






for i in range(1000):
    #print(i, test)
    test = make_test()
    start_time = time.time()
    solution(**test)
    print(time.time() - start_time)
    print('=====================================')




























