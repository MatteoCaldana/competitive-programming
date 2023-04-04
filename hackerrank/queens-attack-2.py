def move(direction, start, obstacles, n):
    if (start == obstacles[direction]) or start[0] < 1 or start[0] > n or start[1] < 1 or start[1] > n:
        return True, start
    newx = direction[0] + start[0]
    newy = direction[1] + start[1]
    return False, (newx, newy)

def enhance(direction, start, obstacles, n):
    blocked = False
    count = -2
    while not blocked:
        blocked, start = move(direction, start, obstacles, n)
        count += 1
    return count

def siftObst(ob,start):
    if ob[0] == start[0]:
        if ob[1] > start[1]:
            return (0,1)
        return (0,-1)
    if ob[1] == start[1]:
        if ob[0] > start[0]:
            return (1,0)
        return (-1,0)
    if (ob[1] - start[1]) == (ob[0] - start[0]):
        if ob[0] > start[0]:
            return (1,1)
        return (-1,-1)
    if (ob[1] - start[1]) == (- ob[0] + start[0]):
        if ob[0] > start[0]:
            return (1,-1)
        return (-1,1)       

    return (0,0)

def reduceObstacles(start, obstacles, n):
    n = n + 1
    result = {(0,1):[(start[0],n)],(0,-1):[(start[0],0)],(1,0):[(n,start[1])],(-1,0):[(0,start[1])],
              (-1,-1):[(0,0)],(1,1):[(n,n)],(-1,1):[(0,n)],(1,-1):[(n,0)]} 
    # sift
    for ob in obstacles:
        direction = siftObst(ob,start)
        if direction != (0,0):
            result[direction].append(tuple(ob))
    #reduce 
    result[(0,1)]=min(result[(0,1)])
    result[(0,-1)]=max(result[(0,-1)])
    result[(1,0)]=min(result[(1,0)])
    result[(-1,0)]=max(result[(-1,0)])
    result[(1,1)]=min(result[(1,1)])
    result[(-1,-1)]=max(result[(-1,-1)])
    result[(-1,1)]=max(result[(-1,1)])
    result[(1,-1)]=min(result[(1,-1)])
    return result

# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
    start = (r_q,c_q)
    obstacles = reduceObstacles(start, obstacles, n)

    result = 0
    for direction in [(0,1),(1,0),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]:
        result += enhance(direction,start,obstacles,n)
    return result


print(queensAttack(4,0,4,4,[]))