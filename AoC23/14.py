with open("14.input", "r") as fp:
    data = fp.read().strip("\n")


def col_load(c):
    l = len(c)
    if l == 0:
        return 0
    if c[0] == "#":
        return col_load(c[1:])
    i = c.find("#")
    i = l if i == -1 else i
    n = l - c[:i].count("O")
    return l * (l + 1) // 2 - n * (n + 1) // 2 + col_load(c[i:])


n = data.find("\n")
sol = 0
for i in range(n):
    col = data[i :: n + 1]
    l = col_load(col)
    sol += l
    print(i, col, l)
print(sol)
