import numpy as np

with open("input.01.day08", "r") as fp:
    data = fp.readlines()

nrows = len(data)
ncols = len(data[0]) - 1

table = dict()

for i in range(nrows):
    for j in range(ncols):
        key = data[i][j]
        if key.isalnum():
            if key in table:
                table[key].append((i, j))
            else:
                table[key] = [(i, j)]


def generate_nodes_all(positions):
    nodes = []
    for i in range(len(positions)):
        for j in range(i):
            nodes += generate_nodes_v2(positions[i], positions[j])
    return nodes

def generate_nodes(node1, node2):
    node1 = np.array(node1)
    node2 = np.array(node2)
    diff = node1 - node2
    
    nodes = [node1 + diff, node2 - diff]
    nodes = [n for n in nodes if n.min() >= 0 and n[0] < nrows and n[1] < ncols]
    nodes = [tuple([*n]) for n in nodes]
    return nodes

def generate_nodes_v2(node1, node2):
    node1 = np.array(node1)
    node2 = np.array(node2)
    diff = node1 - node2

    nodes = [node1, node2]
    n = node1 + diff
    while n.min() >= 0 and n[0] < nrows and n[1] < ncols:
        nodes.append(n.copy())
        n += diff

    n = node2 - diff
    while n.min() >= 0 and n[0] < nrows and n[1] < ncols:
        nodes.append(n.copy())
        n -= diff
    
    nodes = [tuple([*n]) for n in nodes]
    return nodes

all_nodes = []
for key in table:
    all_nodes += generate_nodes_all(table[key])

all_nodes = list(set(all_nodes))
print(len(all_nodes))

see = np.zeros((nrows, ncols))
for i, j in all_nodes:
    see[i, j] = 1
print(see)