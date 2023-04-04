# -*- coding: utf-8 -*-
with open("MissingNumbers_input1.txt",'r') as f:
    indata = f.read()

with open("MissingNumbers_output1.txt",'r') as f:
    outdata = f.read()
    
indata = indata.split('\n')
indata = [[int(j) for j in i.split(' ')] for i in indata[1::2]]
outdata = outdata.split('\n')

def count(l):
    res = [0]*(max(l)+1)
    for i in range(len(l)):
        res[l[i]] += 1
    return res

# Complete the missingNumbers function below.
def missingNumbers(arr, brr):
    count_arr = count(arr)
    count_brr = count(brr)
    
    print(count_arr[3685])
    print(count_brr[3685])
    
    count_arr += [0]*(len(count_brr)-len(count_arr))

    res = []
    for i in range(len(count_arr)):
        for _ in range(count_brr[i]-count_arr[i]):
            res.append(i)
    return res

res = missingNumbers(*indata)