# -*- coding: utf-8 -*-

with open("MorganandaString_input4.txt",'r') as f:
    indata = f.read()

with open("MorganandaString_output4.txt",'r') as f:
    outdata = f.read()
    
indata = indata.split('\n')[1:]
outdata = outdata.split('\n')

def morganAndString(a, b):
    a = list(reversed(list(a)))
    b = list(reversed(list(b)))
    res = []
    k = 0
    while len(a)*len(b) > 0:
        if a[-1] > b[-1]:
            res.append(b.pop())
        elif a[-1] < b[-1]:
            res.append(a.pop())
        else:
            if a[-2] > b[-2]:
                res.append(b.pop())
            else:
                res.append(a.pop())
        if k > 3590 and k < 3610:
            print("==================================")
            print(k)
            print(a[-50:])
            print(b[-50:])
            print(res[-50:])
        k += 1

    res += list(reversed(a)) + list(reversed(b))

    return ''.join(res)


res = morganAndString(indata[6], indata[7])

for i in range(len(res)):
    if res[i] != outdata[3][i]:
        print(i, res[i], outdata[3][i])
        break



