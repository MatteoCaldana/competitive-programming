import numpy as np

with open("9.input", "r") as fp:
    data = fp.read().splitlines()

def parse(data):
    r = []
    for line in data:
        r.append(np.array([int(x) for x in line.split(" ")], dtype=np.int32))
    return r

def solve_line_naive(line):
    hist = [line]
    while not np.all(hist[-1] == 0):
        hist.append(np.diff(hist[-1]))
    
    curr = 0
    for i in range(len(hist) - 2, -1, -1):
        curr += hist[i][-1]

    return curr

def solve_line_naive2(line):
    hist = [line]
    while not np.all(hist[-1] == 0):
        hist.append(np.diff(hist[-1]))
    
    curr = hist[-2][0]
    for i in range(len(hist) - 3, -1, -1):
        curr = hist[i][0] - curr

    return curr

data = parse(data)
sols = []
for line in data:
    sols.append(solve_line_naive2(line))
print(sum(sols))