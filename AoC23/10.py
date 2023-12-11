from collections import deque

with open("10.input", "r") as fp:
    data = fp.read().splitlines()


def inside(data, i, j):
    return i >= 0 and j >= 0 and i < len(data) and j < len(data[0])


def parse(data):
    start = None
    graph = dict()

    for y in range(len(data)):
        for x in range(len(data[0])):
            coord = (x, y)
            graph[coord] = []

            if data[y][x] == "S":
                start = coord
            elif data[y][x] == "|":
                graph[coord].extend([(x, y - 1), (x, y + 1)])
            elif data[y][x] == "-":
                graph[coord].extend([(x - 1, y), (x + 1, y)])
            elif data[y][x] == "L":
                graph[coord].extend([(x, y - 1), (x + 1, y)])
            elif data[y][x] == "J":
                graph[coord].extend([(x, y - 1), (x - 1, y)])
            elif data[y][x] == "7":
                graph[coord].extend([(x, y + 1), (x - 1, y)])
            elif data[y][x] == "F":
                graph[coord].extend([(x, y + 1), (x + 1, y)])

    for coord in graph.keys():
        if start in graph[coord]:
            graph[start].append(coord)
    return start, graph


def dijkstra(data):
    start, graph = parse(data)

    visited = set()
    q = deque()
    q.append((start, 0))
    max_distance = 0

    while len(q):
        node, distance = q.popleft()

        if node in visited:
            continue

        visited.add(node)

        max_distance = max(max_distance, distance)

        for neighbor in graph[node]:
            q.append((neighbor, distance + 1))

    return max_distance


print(dijkstra(data))
