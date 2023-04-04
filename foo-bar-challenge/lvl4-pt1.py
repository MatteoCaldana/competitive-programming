# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 08:21:12 2021

@author: matteo.caldana
"""

# NOTES
# - the path is an adiecency matrix of a graph
# - need to solve a max flow problem (well known in literature)

# Start using the basic Ford–Fulkerson algorithm:
# I do not recall the details so I check Wikipedia
# https://en.wikipedia.org/wiki/Ford%E2%80%93Fulkerson_algorithm

# There is an implementation of Edmonds–Karp algorithm
# Complexity of O(|V||E|^2) is fine as a starting point (V number of vertexes, E number of edges)

# Some improvements could be made to this implementation (like not using a float 
# for path flow) but nothing big.
import collections

class Graph:
    """This class represents a directed graph using adjacency matrix representation."""

    def __init__(self, graph):
        self.graph = graph  # residual graph
        self.row = len(graph)

    def bfs(self, s, t, parent):
        """Returns true if there is a path from source 's' to sink 't' in
        residual graph. Also fills parent[] to store the path."""

        # Mark all the vertices as not visited
        visited = [False] * self.row

        # Create a queue for BFS
        queue = collections.deque()

        # Mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True

        # Standard BFS loop
        while queue:
            u = queue.popleft()

            # Get all adjacent vertices of the dequeued vertex u
            # If an adjacent has not been visited, then mark it
            # visited and enqueue it
            for ind, val in enumerate(self.graph[u]):
                if (visited[ind] == False) and (val > 0):
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u

        # If we reached sink in BFS starting from source, then return
        # true, else false
        return visited[t]

    # Returns the maximum flow from s to t in the given graph
    def edmonds_karp(self, source, sink):

        # This array is filled by BFS and to store path
        parent = [-1] * self.row

        max_flow = 0  # There is no flow initially

        # Augment the flow while there is path from source to sink
        while self.bfs(source, sink, parent):

            # Find minimum residual capacity of the edges along the
            # path filled by BFS. Or we can say find the maximum flow
            # through the path found.
            path_flow = float("Inf")
            s = sink
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            # Add path flow to overall flow
            max_flow += path_flow

            # update residual capacities of the edges and reverse edges
            # along the path
            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow
        
###################################################################################

# Still it is not appliable since, one source and one sink is needed and 
# here are passed as an array
# my idea:
def make_graph(entrances, exits, path):
    # the idea is to have a graph with a unique source and sink
    # thus I collect all the exist in a unique sink node, where the 
    # max flow possible is pratically infinite; and I pre-pend to 
    # all the entrances node a source node
    graph = path
    source = [0]
    for i in range(len(graph)):
        if i in entrances:
            source.append(sum(graph[i]))
        else:
            source.append(0)
        if i in exits:
            graph[i] = [0]+graph[i]+[2000000*50+1]
        else:
            graph[i] = [0]+graph[i]+[0]
    graph.insert(0, source+[0])
    graph.append([0]* (len(graph)+1) )
    return graph

def solution(entrances, exits, path):
    path = make_graph(entrances, exits, path)
    g = Graph(path)
    return g.edmonds_karp(0, len(path)-1)
    

test1 = {
    "entrances": [0], 
    "exits": [3], 
    "path": [
        [0, 7, 0, 0], 
        [0, 0, 6, 0], 
        [0, 0, 0, 8], 
        [9, 0, 0, 0]
    ]
}

test2 = {
    "entrances": [0, 1],
    "exits": [4, 5],
    "path": [
  [0, 0, 4, 6, 0, 0],  # Room 0: Bunnies
  [0, 0, 5, 2, 0, 0],  # Room 1: Bunnies
  [0, 0, 0, 0, 4, 4],  # Room 2: Intermediate room
  [0, 0, 0, 0, 6, 6],  # Room 3: Intermediate room
  [0, 0, 0, 0, 0, 0],  # Room 4: Escape pods
  [0, 0, 0, 0, 0, 0]   # Room 5: Escape pods
]}

test = test2

print(solution(**test))




































