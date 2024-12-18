import re
import numpy as np

with open("input.01.day15", "r") as fp:
    data = fp.read()

idx = data.find("\n\n")
grid = [[x for x in line] for line in data[:idx].split("\n")]
moves = data[idx:].replace("\n", "")


def solve1(grid):

    for i, line in enumerate(grid):
        for j, c in enumerate(line):
            if c == "@":
                ii, jj = i, j

    grid = np.array(grid)

    def move(i, j, m):
        if m == "^":
            next = grid[:i, j][::-1]
            di, dj = -1, 0
        elif m == ">":
            next = grid[i, j + 1 :]
            di, dj = 0, 1
        elif m == "<":
            next = grid[i, :j][::-1]
            di, dj = 0, -1
        elif m == "v":
            next = grid[i + 1 :, j]
            di, dj = 1, 0
        else:
            raise ValueError("")

        idx = np.where(next != "O")[0][0]
        block = next[idx]
        if block == "#":
            return i, j
        else:
            grid[i, j] = "."
            grid[i + di * (idx + 1), j + dj * (idx + 1)] = "O"
            i = i + di
            j = j + dj
            grid[i, j] = "@"
            return i, j

    print("\n".join(["".join(row) for row in grid]))
    for m in moves:
        ii, jj = move(ii, jj, m)

    gps = 0
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i, j] == "O":
                gps += 100 * i + j

    print(gps)


solve1(grid)

grid = [
    [x for x in line]
    for line in data[:idx]
    .translate(str.maketrans({"#": "##", ".": "..", "O": "[]", "@": "@."}))
    .split("\n")
]
moves = data[idx:].replace("\n", "")


def probe(grid, ii, jj, di, dj):
    ni = ii + di
    nj = jj + dj
    if grid[ni][nj] == ".":
        return True
    if grid[ni][nj] == "#":
        return False
    if dj == -1 and grid[ni][nj] == "]":
        return probe(grid, ni, nj - 1, di, dj)
    if dj == 1 and grid[ni][nj] == "[":
        return probe(grid, ni, nj + 1, di, dj)
    # dj == 0
    if grid[ni][nj] == "]":
        return probe(grid, ni, nj, di, dj) and probe(grid, ni, nj - 1, di, dj)
    elif grid[ni][nj] == "[":
        return probe(grid, ni, nj, di, dj) and probe(grid, ni, nj + 1, di, dj)
    else:
        raise ValueError("")


def push(grid, ii, jj, di, dj):
    ni = ii + di
    nj = jj + dj
    if grid[ni][nj] == ".":
        grid[ii][jj], grid[ni][nj] = ".", grid[ii][jj]
        return
    if grid[ni][nj] == "#":
        return
    if dj == -1:
        if grid[ni][nj] == "]":
            push(grid, ni, nj - 1, di, dj)
            grid[ii][jj], grid[ni][nj], grid[ni][nj - 1] = (
                grid[ni][nj - 1],
                grid[ii][jj],
                grid[ni][nj],
            )
            return
    if dj == 1:
        if grid[ni][nj] == "[":
            push(grid, ni, nj + 1, di, dj)
            grid[ii][jj], grid[ni][nj], grid[ni][nj + 1] = (
                grid[ni][nj + 1],
                grid[ii][jj],
                grid[ni][nj],
            )
            return
    # dj == 0
    if grid[ni][nj] == "]":
        push(grid, ni, nj, di, dj)
        push(grid, ni, nj - 1, di, dj)
        grid[ii][jj], grid[ni][nj] = grid[ni][nj], grid[ii][jj]
        return
    elif grid[ni][nj] == "[":
        push(grid, ni, nj, di, dj)
        push(grid, ni, nj + 1, di, dj)
        grid[ii][jj], grid[ni][nj] = grid[ni][nj], grid[ii][jj]
        return


for i, line in enumerate(grid):
    for j, c in enumerate(line):
        if c == "@":
            ii, jj = i, j

MOVE_TABLE = {"<": (0, -1), "^": (-1, 0), ">": (0, 1), "v": (1, 0)}
for mv in moves:
    di, dj = MOVE_TABLE[mv]
    if probe(grid, ii, jj, di, dj):
        push(grid, ii, jj, di, dj)
        ii += di
        jj += dj

gps = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "[":
            gps += 100 * i + j

print(gps)
