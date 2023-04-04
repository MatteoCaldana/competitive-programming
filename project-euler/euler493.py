# -*- coding: utf-8 -*-

#   E[number of distinct colours in 20 randomly picked balls]
# = E[I(A_1) + ... + I(A_7)] 
#   where I(A_i) = indicator function ("there is at least one ball of the i-th color in the 20 extracted")
# = 7 * E[I(A_1)] since the colors are independent
# = 7 * P(A_1) by definition of lebesgue integral
# to evaluate A_i consider a problem with 70 balls of two colors: 10 of color i and 60 of color black
# P(A_i) = 1 - P("all black balls") = 1 - 60/70 * 59/69 * 58/68 * ... * 41/51

from fraction import Fraction

P_all_black_balls = 1
for i in range(20):
    P_all_black_balls = P_all_black_balls * Fraction(60-i,70-i)
    
result = 7*(1 - P_all_black_balls).approx()
