from math import lcm

with open("8.input", "r") as fp:
    data = fp.read().splitlines()

def parse(data):
    tree = dict()
    for line in data[2:]:
        tree[line[:3]] = (line[7:10], line[12:15]) 
    return [{"R": 1, "L": 0}[c] for c in data[0]], tree

def sol1(data):
    seq, tree = parse(data)
    current = "AAA"
    count = 0
    while current != "ZZZ":
        current = tree[current][seq[count % len(seq)]]
        count += 1
    return count

print(sol1(data))

def sol2(data):
    seq, tree = parse(data)
    currents = [key for key in tree if key[2] == "A"]
    counts = []
    for c in currents:
        count = 0
        while c[-1] != "Z":
            c = tree[c][seq[count % len(seq)]]
            count += 1
        counts.append(count)
    return counts

print(lcm(*sol2(data)))
