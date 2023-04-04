# -*- coding: utf-8 -*-

table_sum = [set(),set([(1,)])]

def sums_count(n, table):
    for i in range(1,n):
        for j in table[n-i]:
            tmp = list(j) + [i]
            tmp.sort()
            table[n].add(tuple(tmp))
    table[n].add((n,))
    return table

#for i in range(2,40):
#    print(i)
#    table_sum.append(set())
#    sums_count(i, table_sum)
    
##############################################################################
# dynamic programming count
    
table = [1] + [0]*100
for diff in range(1,100):
    for i in range(diff,101):
        table[i] += table[i - diff]