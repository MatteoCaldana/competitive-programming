# first observation:
# there is a similar text two times: is this relevant?

# seconnd observation:
# to have accurate result we need to have 100 digits of sqrt(2)

# third observation:
# to avoid to use the floor operatin and floating point numbers
# I can write floor(k*sqrt(2)) as
#         int(10**100 * sqrt(2)) * k // 10**100
# where (10**100 * sqrt(2)) is an integer constant, calculated once

# The problem is now to evaluate the 
#         sum(k=1,...,n; A*k//10**100)

# still too many operatins, need to find a way to simplify summation

# Try to bring out the division

# sum(k=1,...,n; A*k//10**100) 
# = sum(k=1,..,n; A*k)//10**100 - sum(k=1,...,n; A*k % 10**100)//10**100
# = A*(n*(n+1)/2) // 10**100 - sum(k=1,...,n; (A-10**100) * k) // 10**100
# = A*(n*(n+1)/2) // 10**100 - (A-10**100) * (n*(n+1)/2) // 10**100

# test this thesis

import math 
import cProfile

def stupid_direct_method(n):
    tot = 0
    for i in range(n):
        tot += math.floor((i+1)*2**0.5)
    return tot

def test_thesis(n):
    exp = 10 # sure fine for double
    A = math.floor((2**0.5)*(10**exp))
    return (A*((n*(n+1))//2)) // 10**exp - (A-10**exp)*((n*(n+1))//2) // 10**exp 
    
# something wrong

def test1(n):
    exp = 10
    A = math.floor((2**0.5)*(10**exp))
    return sum([(A*k)//10**exp for k in range(n+1)])

def test2(n):
    exp = 10
    A = math.floor((2**0.5)*(10**exp))
    B = 10**exp
    return sum([(A*k) for k in range(n+1)]) // B - sum([(A*k) % B for k in range(n+1)]) // B

def test3(n):
    exp = 10
    A = math.floor((2**0.5)*(10**exp))
    B = 10**exp
    return A*((n*(n+1))//2) // B - sum([(A*k) % B for k in range(n+1)]) // B

def test4(n):
    exp = 10
    A = math.floor((2**0.5)*(10**exp))
    B = 10**exp
    return A*((n*(n+1))//2) // B - sum([(A%B) * (k%B) for k in range(n+1)]) // B

# forgot a modulus
# = sum(k=1,..,n; A*k)//10**100 - sum(k=1,...,n; A*k % 10**100)//10**100
# = A*(n*(n+1)/2) // 10**100 - sum(k=1,...,n; ((A-10**100) * k) % 10**100) // 10**100
# = A*(n*(n+1)/2) // 10**100 - ...
# I can simplify the second part by knowing the minimum common multiple of (A-10**100) and 10**100

# start by computing sqrt(2) to needed precision
# Newton's method has second order convergence, so about 10 iterations are fine
# X^2 -2 = 0
# x_n+1 = x_n - f(x_n)/f'(x_n)
# x_n+1 = (x_n-2)^2/(2x_n)

def gcd(a, b):
    while a != b: 
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

def step(num, den):
    n = num*num + 2*den*den
    d = 2*den*num 
    GCD = gcd(n,d)
    return n//GCD, d//GCD

def compute_sqrt_2(n):
    exp = 10
    num, den = math.floor(2*0.5*10**exp), 10**exp
    for i in range(n):
        num, den = step(num, den)
    return num, den

def compute_repr(num, den):
    repres = ''
    for i in range(201):
        repres += str(num // den)
        num = (num % den) *10
    return repres

# A and 10**100 are co-prime
# = A*(n*(n+1)/2) // 10**100 - sum(k=1,...,n; ((A-10**100) * k) % 10**100) // 10**100
# = A*(n*(n+1)/2) // 10**100 - (n(n+1)/2 * (A-10**100) - ? * 10**100) // 10**100

# the reminders (C:=(A-10**100), B:= 10**100) in the sum sum(k=1,...,n; ((A-10**100) * k) % 10**100)
# C
# 2C
# 3C - B
# ...
# nC - (nC/B)B -> there is (nC/B) as coef for untill C has as coef (nC/B)B)/C (diff in that point)

def compute_num_bs(n, C, B):
    num_bs = 0
    while n > 1:
        coef_b = (n*C)//B
        coef_c = (coef_b * B) // C
        
        if coef_c == n:
            num_bs += coef_b
            n -= 1
        else:
            num_bs += (n - coef_c) * coef_b
            n = coef_c
                
    return num_bs

def compute_sum(n, sqrt2):
    sum_n = (n*(n+1))//2
    exp = len(str(sum_n)) + 1
    sqrt2 = sqrt2[:exp]
    A = int(sqrt2)
    B = 10**(exp-1)
    C = A - B
    return A*sum_n // B - ( sum_n*C - compute_num_bs(n, C, B)*B ) // B
    
# since I use sum_n*A, I need more precision with sqrt(2)

###############################################################################
###############################################################################

# this is still too slow
# searching on oeis some of the sequences that I obtained, I found that this 
# sequence is called: Beatty sequence
# https://oeis.org/A001951
# https://en.wikipedia.org/wiki/Beatty_sequence

# Define the successions
#                           a_k = floor(sqrt(2)*k)
#                           b_k = floor((2+sqrt(2))*k)      # called complementary succession of a_k
# And their partial sums
#                           A_k = sum(i=0,...,k; a_k)
#                           B_k = sum(i=0,...,k; b_k)
# Then thanks to Rayleigh theorem, we know that a_k and b_k_1 makes a partition of
# all integers smaller than a_k, where k_1 is the max i in N (naturals) such that 
# the complementary succession is smaller than the one we want to calculate, i.e.
#                           k_1 = max(i in N) s.t. b_i < a_k 
# Then A_k + B_k_1 is the sum of all integers smaller or equal than a_k, thus
#                           A_k + B_k_1 = a_k*(a_k+1)/2
# But we also have that
#                           B_k_1 = A_k_1 + sum(i=0,...,k_1 2*i) = A_k_1 + k_1(k_1+1)
# by definition of the successions.
# Then we have:
#                           A_k + A_k_1 = a_k*(a_k+1)/2 - k_1(k_1+1)
# Fist thing observe that k_1 is about sqrt(2)/(2+sqrt(2)) times k
# Second it also holds that
#                           A_k_1 + A_k_2 = a_k_1*(a_k_1+1)/2 - k_2(k_2+1)
# where k_2 is the max(i in N) s.t. b_i < a_k_1
# Notice that we can iterate writing this equations until k_n is known
# Since each time k_n+1 is a fraction of k_n it has exponential convergence (O(log N) complexity)
# Thus we can sum all this together, one time with positive sing, one time with 
# negative sign, so that the terms on the LHS cancel out. Namely on the LHS we have
#                          A_k + A_k_n = ...
# Since we are interested in A_k we can keep track of the terms
#                          a_k_n*(a_k_n+1)/2 - k_{n+1}(k_{n+1}+1)
# and in the end subtract (or sum depending if the last eq. was subtracted or added) A_k_n


def generate_beatty(idx, beatty_coef):
    res = [0]
    for i in range(1, idx+1):
        res.append(math.floor(i*beatty_coef))
    return res
    
def sqrt2_floor(n):
    _sqrt2 = '1414213562373095048801688724209698078569671875376948073176679737990732478462107038850387534327641572735013846230912297024924836055850737212644121497099935831413222665927505592755799950501152782060571470109559971605970274534596862014728517418640889198609552329230484308714321450839762603627995251407989687253396546331808829640620615258352395054745750287759961729835575220337531857011354374603408498847160'

    n_str = str(n)
    exp = len(n_str)*2+2
    sqrt2 = int(_sqrt2[:exp])
    return (n*sqrt2)//10**(exp-1)

# given n = floor(sqrt2*m), I want to find the biggest k s.t. 2k+floor(sqrt2*k) < n
def find_complementary_index(n):
    _sqrt2 = '1414213562373095048801688724209698078569671875376948073176679737990732478462107038850387534327641572735013846230912297024924836055850737212644121497099935831413222665927505592755799950501152782060571470109559971605970274534596862014728517418640889198609552329230484308714321450839762603627995251407989687253396546331808829640620615258352395054745750287759961729835575220337531857011354374603408498847160'
    #generate_beatty(find_complementary_index(str(_Bs[-1])), 2+2**0.5)
    _b_k = [0, 3, 6, 10, 13, 17, 20, 23, 27, 30, 34, 37, 40, 44, 47, 51, 54, 58, 61, 64, 68, 71, 75, 78, 81, 85, 88, 92, 95, 99, 102]
    
    n_str = str(n)
    if n <= _b_k[-1]:
        for i in range(min(len(_b_k)*(_b_k[-1]/n)+3, len(_b_k)-1), 0, -1):
            if _b_k[i] < n:
                return i
    den = _sqrt2[:len(n_str)-2]
    ub = (n*10**(len(den)-1)) // int('3'+den[1:])
    a_ub = sqrt2_floor(ub)
    while 2*ub + a_ub > n:
        ub -= 1
        a_ub = sqrt2_floor(ub)
    return ub, a_ub

def compute_solution(n):
    A = [0, 1, 3, 7, 12, 19, 27, 36, 47, 59, 73, 88, 104, 122, 141, 162, 184, 208, 
         233, 259, 287, 316, 347, 379, 412, 447, 483, 521, 560, 601, 643, 686, 731, 
         777, 825, 874, 924, 976, 1029, 1084, 1140, 1197, 1256, 1316, 1378, 1441, 
         1506, 1572, 1639, 1708, 1778, 1850, 1923, 1997, 2073, 2150, 2229, 2309, 
         2391, 2474, 2558, 2644, 2731, 2820, 2910, 3001, 3094, 3188, 3284, 3381, 
         3479, 3579, 3680, 3783, 3887, 3993, 4100, 4208, 4318, 4429, 4542, 4656, 
         4771, 4888, 5006, 5126, 5247, 5370, 5494, 5619, 5746, 5874, 6004, 6135, 
         6267, 6401, 6536, 6673, 6811, 6951]

    solution = 0
    a_k = sqrt2_floor(n)
    curr = 0
    while a_k > 140: # 140 = sqrt2_floor(len(A))
        k_new, a_k_new = find_complementary_index(a_k)
        solution += (1 if curr % 2 == 0 else -1)*((a_k*(a_k+1))//2 - k_new*(k_new+1))
        
        a_k = a_k_new
        curr += 1
    return solution + (1 if curr % 2 == 0 else -1)*A[k_new]


def solution(s):
    s = int(s)
    
    A = [0, 1, 3, 7, 12, 19, 27, 36, 47, 59, 73, 88, 104, 122, 141, 162, 184, 208, 
         233, 259, 287, 316, 347, 379, 412, 447, 483, 521, 560, 601, 643, 686, 731, 
         777, 825, 874, 924, 976, 1029, 1084, 1140, 1197, 1256, 1316, 1378, 1441, 
         1506, 1572, 1639, 1708, 1778, 1850, 1923, 1997, 2073, 2150, 2229, 2309, 
         2391, 2474, 2558, 2644, 2731, 2820, 2910, 3001, 3094, 3188, 3284, 3381, 
         3479, 3579, 3680, 3783, 3887, 3993, 4100, 4208, 4318, 4429, 4542, 4656, 
         4771, 4888, 5006, 5126, 5247, 5370, 5494, 5619, 5746, 5874, 6004, 6135, 
         6267, 6401, 6536, 6673, 6811, 6951]

    if s < len(A):
        return str(A[s])
    return str(compute_solution(s))

###############################################################################

for i in range(10000):
    s1 = solution(i)
    s2 = str(stupid_direct_method(i))
    if s1 != s2:
        print(i, s1, s2)
    if i % 100 == 0:
        print('----',i)

#cProfile.run('solution(100000000000000)')
    