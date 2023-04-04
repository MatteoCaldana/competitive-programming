def d(n):
  res = 0
  while n > 0:
    res += n % 10
    n //= 10
  return res

def dd(n):
  return n / d(n)

def F(n):
  res = 0
  for i in range(n):
    res += dd(i+1)
  return res

n = 1234567890123456789
UB = n*(n+1)//2
print((UB // 10**12)**.5)

## try estimate by interpolation
def ex(n):
  print(F(n), n*(n+1)//2 / F(n))

ex(10)
ex(123)
ex(1234)
ex(12345)
ex(123456)
ex(1234567)
ex(12345678)

print(n*(n+1)//2 / 90)
#res = 0
#for i in range(n, 0, -1):
#  res += dd(i)
#  if i % 100000 == 0:
#    print(res, dd(i) / res, res + i * dd(i))
