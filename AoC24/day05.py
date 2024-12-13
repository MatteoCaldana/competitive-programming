import re
import numpy as np

with open("input.01.day05", "r") as fp:
    data = fp.readlines()

rules = []
pages = []

idx = -1
for i, line in enumerate(data):
    if line == "\n":
        idx = i
        break

    rules.append([int(x) for x in line.split("|")])

for i in range(idx + 1, len(data)):
    pages.append([int(x) for x in data[i].split(",")])

print(rules)
print(pages)

def check_sorted(table, rules):
    ok = True
    for p1, p2 in rules:
        if p1 in table and p2 in table:
            if table[p1] > table[p2]:
                ok = False
    return ok

def fix(pages, table, rules):
    ok = True
    for p1, p2 in rules:
        if p1 in table and p2 in table:
            if table[p1] > table[p2]:
                pages[table[p1]], pages[table[p2]] = pages[table[p2]], pages[table[p1]]
                table[p1], table[p2] = table[p2], table[p1]
    return ok

middles = []
for page in pages:
    table = {p: i for i, p in enumerate(page)}
    ok = check_sorted(table, rules)
    if ok:
        middles.append(page[len(page)//2])


print(sum(middles))

import networkx as nx
from functools import cmp_to_key

G = nx.DiGraph()
G.add_edges_from(rules)
print("is connected: ", nx.is_strongly_connected(G))

def comparator(a, b):
    if a == b:
        return 0 
    if nx.has_path(G, a, b):
        return -1
    else:
        return 1

middles = []
for page in pages:
    table = {p: i for i, p in enumerate(page)}
    ok = check_sorted(table, rules)
    if not ok:
        while not check_sorted(table, rules):
            fix(page, table, rules)

        middles.append(page[len(page)//2])

print(sum(middles))
