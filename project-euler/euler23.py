from utils import list_divisors

#print(list_divisors(12))
def is_abundant(n):
    d = list_divisors(n)
    d.sort()
    sd = sum(d[0:-1])
    if sd > n:
        return True
    return False


l = []
for i in range(28124):
    if(is_abundant(i)):
        l.append(i)

print(l[4000])

all_sums = set()
for i in range(4000):
    for j in range(i, len(l)):
        all_sums.add(l[i]+l[j])

sol = 0
for i in range(28124):
    if i not in all_sums:
        sol += i

print(sol)
