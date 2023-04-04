# -*- coding: utf-8 -*-

pattern = "1234567890"

for i in range(int(1020304050607080900**0.5),int(1929394959697989990**0.5)+1):
    if i % 1000000 == 0:
        print(i//1000000)
    if str(i**2)[::2] == pattern:
        print(i)
        break
        

