import copy
import itertools

with open("input.01.day07", "r") as fp:
    data = fp.readlines()

data = [line.split(": ") for line in data]
data = [(int(line[0]), [int(x) for x in line[1].split(" ")]) for line in data]

def generate_opts(n):
    table = ["+"]*n
    opts = []
    for i in range(2**n):
        for j in range(n):
            table[j] = "*" if (i & (1 << j)) else "+"
        opts.append(copy.deepcopy(table))
    return opts

TABLE = []
for n in range(15):
    TABLE.append(generate_opts(n))

sum = 0
for line in data:
    tokens = line[1]
    for choice in TABLE[len(tokens) - 1]:
        tmp = tokens[0]
        for i, token in enumerate(tokens[1:]):
            if choice[i] == "+":
                tmp += token
            else:
                tmp *= token

        if tmp == line[0]:
            sum += line[0]
            break

print(sum)

sum = 0
for id, line in enumerate(data):
    print(id, len(data))
    tokens = line[1]
    for choice in itertools.product("+*|", repeat=len(tokens) - 1):
        tmp = tokens[0]
        for i, token in enumerate(tokens[1:]):
            if choice[i] == "+":
                tmp += token
            elif choice[i] == "*":
                tmp *= token
            else:
                tmp = int(str(tmp)+str(token))

            if tmp > line[0]:
                break

        if tmp == line[0]:
            sum += line[0]
            break

print(sum)