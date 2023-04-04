# -*- coding: utf-8 -*-

# 10**n has n+1 digits

m = 1
while len(str(9**m)) == m:
    m += 1

result = 0
for i in range(1,m):
    for j in range(1,10):
        if len(str(j**i)) == i:
            result += 1
