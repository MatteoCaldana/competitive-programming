MAX = 2**32

def build_table(mm, init):
    table = []
    for i in range(len(mm)):
        table.append([])
        for j in range(len(mm[i])):
            table[i].append(init)
    return table
    
def dijkstra(mm):
    rows, cols = len(mm), len(mm[0])
    
    dist = build_table(mm, MAX)
    dist[0][0] = 1
    prev = build_table(mm, (-1,-1))
    
    verts = [(i,j) for i in range(rows) for j in range(cols) if mm[i][j] == 0]
    done = [0] * len(verts)
    while sum(done) < len(done):
        v, d, idx = (-1,-1), MAX+1, -1
        for i in range(len(verts)):
            x, y = verts[i]
            if (not done[i]) and dist[x][y] < d:
                v = (x,y)
                d = dist[x][y]
                idx = i
        done[idx] = 1
        
        for dx, dy in [(0,1),(1,0),(-1,0),(0,-1)]:
            x, y = v[0] + dx, v[1] + dy
            if (x >= 0 and x < rows and y >= 0 and y < cols) and (mm[x][y] == 0):
                curr_dist = dist[v[0]][v[1]] + 1
                if curr_dist < dist[x][y]:
                    dist[x][y] = curr_dist
                    prev[x][y] = v
                    
    return dist, prev

def find_best_wall_to_remove(mm, dist, path):
    rows, cols = len(mm), len(mm[0])
    save = 0
    wall_to_remove = (-1,-1)
    for i in range(rows):
        for j in range(cols):
            if mm[i][j] == 1:
                surrounding_dist = []
                for dx, dy in [(0,1),(1,0),(-1,0),(0,-1)]:
                    x, y = i + dx, j + dy
                    if (x >= 0 and x < rows and y >= 0 and y < cols) and (mm[x][y] == 0) and ((x,y) in path):
                       surrounding_dist.append(dist[x][y])
                if len(surrounding_dist):
                    curr_save = max(surrounding_dist) - min(surrounding_dist) - 2
                    if curr_save > save:
                        save = curr_save
                        wall_to_remove = (i,j)
    return save, wall_to_remove
    
def path_list(prev):
    path = [(len(prev)-1, len(prev[0])-1)]
    while path[-1] != (-1,-1):
        i, j = path[-1]
        path.append(prev[i][j])
    return path
    
def find_thin_walls(mm):
    rows, cols = len(mm), len(mm[0])
    thin_walls = []
    for i in range(rows):
        for j in range(cols):
            if mm[i][j] == 1:
                surroundings = 0
                for dx, dy in [(0,1),(1,0),(-1,0),(0,-1)]:
                    x, y = i + dx, j + dy
                    if (x >= 0 and x < rows and y >= 0 and y < cols) and (mm[x][y] == 0):
                       surroundings += 1
                if surroundings > 1:
                    thin_walls.append((i,j))
    return thin_walls
                    
def solution(mm):
    dist, prev = dijkstra(mm)
    abs_min = (len(dist) + len(dist[0]) - 1)
    d = dist[len(dist)-1][len(dist[0])-1]
    if d == abs_min:
        print("abs_min")
        return d
    else:
        min_d = d
        walls = find_thin_walls(mm)
        print(walls)
        for i, j in walls:
            mm[i][j] = 0
            print(i, j, mm[i][j], mm)
            dd, pp = dijkstra(mm)
            newd = dd[len(dd)-1][len(dd[0])-1]
            print("newd",newd)
            if newd < min_d:
                min_d = newd
            if newd == abs_min:
                return abs_min
            mm[i][j] = 1
        print("min_d")
        return min_d

test1 = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]
test2 = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]

test = test2

print(solution(test))