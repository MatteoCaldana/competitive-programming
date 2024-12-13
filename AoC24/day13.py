import re
import numpy as np

with open("input.01.day13", "r") as fp:
    data = fp.read()

pattern = pattern = r"Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)"

matches = re.findall(pattern, data)
print(matches)

matches = [[int(x) for x in p] for p in matches]

def solve(p):
    A = np.array(p[:4]).reshape((2, 2)).T
    b = np.array(p[4:])
    x = np.linalg.solve(A, b).round()
    return 0 if not (A @ x == b).all() else np.dot(x, [3, 1])

for p in matches:
    p[-1] += 10000000000000
    p[-2] += 10000000000000

cs = []
for i, p in enumerate(matches):
    print(i)
    cs.append(solve(p))

print(cs)
print(sum(cs))
