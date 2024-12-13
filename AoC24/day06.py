import numpy as np
import copy

with open("input.01.day06", "r") as fp:
    data = fp.readlines()

print(data)

for i in range(len(data)):
    j_idx = data[i].find("^")
    if j_idx != -1:
        i_idx = i
        break

assert(data[i_idx][j_idx] =="^")

visited = np.zeros((len(data), len(data[0]) - 1), dtype=np.int32)
initial_state = (i_idx, j_idx, "^")
state = initial_state

def is_inside(state):
    i_idx, j_idx, dir = state
    if i_idx == 0 and dir == "^":
        return False
    if i_idx == visited.shape[0] - 1 and dir == "v":
        return False
    if j_idx == 0 and dir == "<":
        return False
    if j_idx == visited.shape[1] - 1 and dir == ">":
        return False
    return True

def move(state, data):
    i_idx, j_idx, dir = state
    if dir == "^":
        if data[i_idx - 1][j_idx] != "#":
            return (i_idx - 1, j_idx, dir)
        else:
            return (i_idx, j_idx, ">")
    if dir == "v":
        if data[i_idx + 1][j_idx] != "#":
            return (i_idx + 1, j_idx, dir)
        else:
            return (i_idx, j_idx, "<")
    if dir == ">":
        if data[i_idx][j_idx + 1] != "#":
            return (i_idx, j_idx + 1, dir)
        else:
            return (i_idx, j_idx, "v")
    if dir == "<":
        if data[i_idx][j_idx - 1] != "#":
            return (i_idx, j_idx - 1, dir)
        else:
            return (i_idx, j_idx, "^")
    
    
def plot(state, data):
    i_idx, j_idx, dir = state
    datacopy = [[x for x in line] for line in data]
    datacopy[i_idx][j_idx] = dir
    print("".join(["".join(line) for line in datacopy]))

while is_inside(state):
    visited[*state[0:2]] = 1
    state = move(state, data)
    #plot(state, data)
    #print("=====================")
visited[*state[0:2]] = 1

print(visited)
print(visited.sum())


loops = 0
for oi in range(visited.shape[0]):
    for oj in range(visited.shape[1]):
        print(oi, oj)
        datacopy = [[x for x in line] for line in data]
        datacopy[oi][oj] = "#"
        table = {initial_state}
        state = initial_state

        while is_inside(state):
            state = move(state, datacopy)
            if state in table:
                loops += 1
                break
            table.add(state)

print(loops)