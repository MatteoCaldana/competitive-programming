
n = input()
 
def nearest_smaller_bin(n):
    sn = str(n)
    for i in range(len(sn)):
        if sn[i] > '1':
            return sn[:i] + ''.join(['1']*(len(sn)-i))
    return sn
    
def to2(n):
    res = 0
    for i in range(len(n)):
        res += (ord(n[i])-ord('0'))*2**(len(n)-i-1)
    return res
    
print(to2(nearest_smaller_bin(n)))