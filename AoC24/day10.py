with open("input.01.day10", "r") as fp:
    data = fp.readlines()

nrows = len(data)
ncols = len(data[0]) - 1
print(nrows, ncols)
print(data)

def inside(x, y):
    return x >= 0 and y >= 0 and x < nrows and y < ncols

def dfs_v1(x, y, data):
    if data[x][y] == "9":
        return [(x, y)]
    paths = []
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        xn = x + dx
        yn = y + dy
        if inside(xn, yn):
            if ord(data[xn][yn]) - ord(data[x][y]) == 1:
                paths += dfs_v1(xn, yn, data)
    return paths

def dfs_v2(x, y, data):
    if data[x][y] == "9":
        return 1
    paths = 0
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        xn = x + dx
        yn = y + dy
        if inside(xn, yn):
            if ord(data[xn][yn]) - ord(data[x][y]) == 1:
                paths += dfs_v2(xn, yn, data)
    return paths

cnt_tot = 0
for i in range(nrows):
    for j in range(ncols):
        if data[i][j] == "0":
            nines = dfs_v1(i, j, data)
            cnt = len(set(nines))
            print(i ,j, cnt)
            cnt_tot += cnt

print(cnt_tot)
            
cnt_tot = 0
for i in range(nrows):
    for j in range(ncols):
        if data[i][j] == "0":
            cnt = dfs_v2(i, j, data)
            print(i ,j, cnt)
            cnt_tot += cnt

print(cnt_tot)