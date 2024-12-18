import numpy as np
import heapq
from collections import defaultdict, deque

np.set_printoptions(linewidth=np.inf)

with open("input.01.day16", "r") as fp:
    data = fp.read()
data = data.split("\n")

rows = len(data)
cols = len(data[0])
visited = np.zeros((rows, cols), dtype=int)
dist = rows * cols * 10000 * np.ones((rows, cols), dtype=int)
for i in range(rows):
    for j in range(cols):
        if data[i][j] == "S":
            si, sj = i, j
        if data[i][j] == "E":
            ei, ej = i, j

dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]
sd = 3
state = ((si, sj), sd)
dist = defaultdict(lambda: rows * cols * 10000)
dist[state] = 0
trace = defaultdict(set)

queue = [(0, state)]
while len(queue):
    dst, state = heapq.heappop(queue)
    ((i, j), sd) = state
    for k, dir in enumerate(dirs):
        ni = i + dir[0]
        nj = j + dir[1]
        new_state = ((ni, nj), k)
        if data[ni][nj] != "#":
            cst = dist[state] + (1 if k == sd else 1001)
            if cst <= dist[new_state]:
                trace[new_state].add(state)
            if cst < dist[new_state]:
                dist[new_state] = cst
                heapq.heappush(queue, (dist[new_state], new_state))

q = deque()
ends = set([((ei, ej), 1)])
q.extend(ends)
tiles = set()
while q:
    node = q.popleft()
    tiles.add(node[0])
    q.extend(trace[node])

table = np.zeros((rows, cols), dtype=int)
for state in dist:
    (i, j), k = state
    table[i, j] = dist[state]
print(table)
for k in range(4):
    print(dist[((ei, ej), k)])
print(len(tiles))
