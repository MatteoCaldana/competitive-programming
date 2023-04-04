from utils import fact

n = 10
l = list(range(0, n))
pos = 999999 # zero based

if pos > fact(n):
    print('error')

for i in range(n - 1):
    needle = pos // fact(n - i - 1)
    print(l[needle], end='')
    l.pop(needle)
    pos = pos % fact(n - i - 1)

print(l[0])

