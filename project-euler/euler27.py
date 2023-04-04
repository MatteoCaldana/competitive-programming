from utils import isprime

def quadratic_form(n, a, b):
    return n*n + a*n + b

def strike_len(a, b):
    i = 0
    while True:
        n = quadratic_form(i + 1, a, b)
        if n < 0:
            break
        if isprime(n):
            i += 1
        else:
            break
    return i

print(strike_len(1, 41))
print(strike_len(-79, 1601))

aa = [0]
bb = [0]
for i in range(1,1001):
    if i % 2 == 1:
        aa += [i, -i]
    if isprime(i):
        bb += [i]

l = []
maxsl = 0
for a in aa:
    for b in bb:
        sl = strike_len(a, b)
        if maxsl < sl:
            maxsl = sl
            print(sl)
        l.append((a, b, sl))

max_strike = max(map(lambda x: x[-1], l))
for i in range(len(l)):
    if l[i][-1] == max_strike:
        print(l[i])

