import numpy as np


with open("input.01.day02", "r") as fp:
    data = fp.readlines()

data = [[int(x) for x in line.split(" ")] for line in data]

def check_line(line):
    return (np.all(np.diff(line) > 0) or np.all(np.diff(line) < 0)) and np.all((np.abs(np.diff(line)) >= 1) & (np.abs(np.diff(line)) <= 3))

cnt = 0
cnt2 = 0
for line in data:
    if check_line(line):
        cnt += 1
        cnt2 += 1
        continue 

    for i in range(len(line)):
        line_copy = np.array([*line[:i], *line[i+1:]])
        assert len(line_copy) == len(line) - 1
        if check_line(line_copy):
            cnt2 += 1
            break

print(cnt)
print(cnt2)
