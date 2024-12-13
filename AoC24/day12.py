import copy
import numpy as np

with open("input.01.day12", "r") as fp:
    data = fp.readlines()

nrows = len(data)
ncols = len(data[0]) - 1
print(nrows, ncols)

data = [(" " * (ncols + 2))] + [" " + l + " " for l in data] + [" " * (ncols + 2)]

data_np = -np.ones((nrows + 2, ncols + 2), dtype=int)
for i in range(1, nrows + 1):
    for j in range(1, ncols + 1):
        data_np[i, j] = ord(data[i][j]) + 2**30
print(data_np)

visited = np.zeros_like(data_np, dtype=int)

id = 0


def inside(x, y):
    return x >= 1 and y >= 1 and x < nrows + 1 and y < ncols + 1


def dfs(i, j, data_np):
    visited[i, j] = True
    for di, dj in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        ni = i + di
        nj = j + dj
        if inside(ni, nj) and not visited[ni, nj]:
            if data_np[ni, nj] == data_np[i, j]:
                dfs(ni, nj, data_np)

    data_np[i, j] = id


for i in range(1, nrows + 1):
    for j in range(1, ncols + 1):
        if data_np[i, j] > 2**30:
            dfs(i, j, data_np)
            id += 1

print(data_np)

table = dict()
default_ele = {"area": 1, "perimeter": 0, "corners": 0}


def n_cross_bnd(i, j, data):
    cnt = 0
    for di, dj in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        ni = i + di
        nj = j + dj
        if data[ni, nj] != data[i, j]:
            cnt += 1
    return cnt


def n_cross_bnd_v2(i, j, data):
    neigh = data[i - 1 : i + 2, j - 1 : j + 2]
    neigh_mask = neigh == data[i, j]
    cnt = 0
    cnt += int((neigh_mask[:2, :2] == np.array([[0, 1], [1, 1]], dtype=bool)).all())
    cnt += int((neigh_mask[:2, :2] == np.array([[0, 0], [0, 1]], dtype=bool)).all())
    cnt += int((neigh_mask[:2, :2] == np.array([[1, 0], [0, 1]], dtype=bool)).all())
    cnt += int((neigh_mask[1:, :2] == np.array([[1, 1], [0, 1]], dtype=bool)).all())
    cnt += int((neigh_mask[1:, :2] == np.array([[0, 1], [0, 0]], dtype=bool)).all())
    cnt += int((neigh_mask[1:, :2] == np.array([[0, 1], [1, 0]], dtype=bool)).all())
    cnt += int((neigh_mask[:2, 1:] == np.array([[1, 0], [1, 1]], dtype=bool)).all())
    cnt += int((neigh_mask[:2, 1:] == np.array([[0, 0], [1, 0]], dtype=bool)).all())
    cnt += int((neigh_mask[:2, 1:] == np.array([[0, 1], [1, 0]], dtype=bool)).all())
    cnt += int((neigh_mask[1:, 1:] == np.array([[1, 1], [1, 0]], dtype=bool)).all())
    cnt += int((neigh_mask[1:, 1:] == np.array([[1, 0], [0, 0]], dtype=bool)).all())
    cnt += int((neigh_mask[1:, 1:] == np.array([[1, 0], [0, 1]], dtype=bool)).all())
    return cnt


vertices = []

for i in range(1, nrows + 1):
    for j in range(1, ncols + 1):
        key = data_np[i, j]
        if key in table:
            table[key]["area"] += 1
        else:
            table[key] = copy.deepcopy(default_ele)
        neigh = n_cross_bnd(i, j, data_np)
        nvtx = n_cross_bnd_v2(i, j, data_np)
        print(i, j, nvtx)
        table[key]["perimeter"] += neigh
        table[key]["corners"] += nvtx



result = 0
result_2 = 0
for key in table:
    result += table[key]["area"] * table[key]["perimeter"]
    result_2 += table[key]["area"] * table[key]["corners"]
    print(table[key]["area"], table[key]["corners"])

print(result)
print(result_2)
