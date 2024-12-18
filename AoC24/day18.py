import numpy as np
import heapq

data = np.genfromtxt("input.01.day18", delimiter=",", dtype=int)
m = 71
grid = np.zeros((m, m), dtype=int)
n = 1024
grid[data[:n, 1], data[:n, 0]] = 1
MAX_DIST = 100000

def inside(ij):
    i, j = ij
    return i >= 0 and j >= 0 and i < m and j < m

def solve(grid):
    si, sj = 0, 0
    state = (si, sj)
    dist = MAX_DIST * np.ones_like(grid)
    dist[*state] = 0
    queue = [(0, state)]
    dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    while len(queue):
        dst, state = heapq.heappop(queue)
        i, j = state
        for k, dir in enumerate(dirs):
            ni = i + dir[0]
            nj = j + dir[1]
            new_state = (ni, nj)
            if inside(new_state) and grid[*new_state] == 0:
                cst = dist[*state] + 1
                if cst < dist[*new_state]:
                    dist[*new_state] = cst
                    heapq.heappush(queue, (dist[*new_state], new_state))

    return dist[(m - 1, m - 1)]

print(solve(grid))

for n in range(1024, 3450):
    grid = np.zeros((m, m), dtype=int)
    grid[data[:n, 1], data[:n, 0]] = 1
    sol = solve(grid)
    print(n, data[n - 1, :], sol)
    if sol == MAX_DIST:
        break
    