import numpy as np

with open("11.input", "r") as fp:
    data = fp.read().strip("\n").splitlines()

data_mat = np.empty((len(data), len(data[0])), dtype=bool)
for i in range(len(data)):
    for j in range(len(data[i])):
        data_mat[i, j] = data[i][j] == "#"

exp_col = np.where(np.sum(data_mat, axis=0) == 0)[0]
exp_row = np.where(np.sum(data_mat, axis=1) == 0)[0]
galax = np.where(data_mat)
galax = np.stack([galax[0], galax[1]])

for i in range(galax.shape[1]):
    galax[0, i] += np.where(exp_row < galax[0, i])[0].size * (1000000 - 1)
    galax[1, i] += np.where(exp_col < galax[1, i])[0].size * (1000000 - 1)

def dist(i, j, galax):
    x1, y1 = galax[:, i]
    x2, y2 = galax[:, j]
    if x2 < x1:
        x1, x2 = x2, x1
    if y2 < y1:
        y1, y2 = y2, y1
    return (x2 - x1) + (y2 - y1)

sol = 0
for i in range(galax.shape[1]):
    for j in range(i):
        d = dist(i, j, galax)
        sol += d

print(sol)
