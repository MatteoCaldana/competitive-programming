with open("15.input", "r") as fp:
    data = fp.read().strip("\n")


def hash(s):
    h = 0
    for c in s:
        h += ord(c)
        h *= 17
        h = h % 256
    return h


sol = 0
lens = [[] for _ in range(256)]
for s in data.split(","):
    sol += hash(s)

    if s[-1] == "-":
        label = s[:-1]
        op = "-"
    else:
        label = s[:-2]
        value = int(s[-1])
        op = "="
    box = hash(label)

    if op == "-":
        for i in range(len(lens[box])):
            if lens[box][i][0] == label:
                del lens[box][i]
                break
    elif op == "=":
        idx = -1
        for i in range(len(lens[box])):
            if lens[box][i][0] == label:
                idx = i
                break
        if idx != -1:
            lens[box][idx] = (label, value)
        else:
            lens[box].append((label, value))
    else:
        raise ValueError("Unknown action: " + op)


print(sol)

sol_2 = 0
for k, box in enumerate(lens):
    if len(box):
        for j, (_, val) in enumerate(box):
            sol_2 += (k + 1) * (j + 1) * val
print(sol_2)