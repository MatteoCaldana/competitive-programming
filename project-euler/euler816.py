import numpy as np
from scipy import spatial

N = 14 #2*10**6
s = np.empty(2*N, dtype=np.uint64)
s[0] = 290797
for i in range(1, s.size):
    s[i] = (s[i-1]**2) % 50515093
print("Points created")

def ss(x, y):
   return x + 2*y
f = np.frompyfunc(ss, 2, 1)
a = f.accumulate(np.arange(10))

# p = s.reshape((-1, 2)).astype(float)
# t = spatial.KDTree(p)
# print("Tree created")

# d = 1e300
# for i, p0 in enumerate(p):
#     d0, i0 = t.query(p0, 2)
#     d = min(d, d0[1])
#     if i % 10000 == 0:
#         print(i)
