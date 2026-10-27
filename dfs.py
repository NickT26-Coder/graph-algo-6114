'''
What is DFS / Topological Sort on a graph?

DFS:
Search "deeper" in the graph whenever possible. Uses a stack to explore the edges of
the most recently discovered node if they have more nodes to explore. Return back to the
original node that was searched once edges have been exhausted and move onto to the next
until all nodes are visited. DFS is used for cycle finding which is determined by presence of a back edge.

Topological Sorting / Ordering:
Topological sorting can only be used on a DAG which DFS is used to confirm whether or not
the graph is cyclical. Uses DFS as DFS keeps track of visited nodes it creates an order of precendence that is
used to order higher priority items first or reverse if needed.

Psuedo Code:

Runtime:

'''

# Implementation
from graph import graphADT

cycles = []

def dfsAlgo(g: graphADT):
    s = []
    visited = []
    for vertex in g.vertices:
        if vertex.color == "WHITE":
            dfsVisit(vertex, s, visited)

    if len(cycles) > 0:
        return cycles
    else:
        topo = []
        while s:
            topo.append(s.pop())

        return topo

def dfsVisit(u: graphADT.vertex, s: list[str], visited: list[str]):
    u.color = "GRAY"
    visited.append(u.data)
    for i in range(len(u.edges)):
        neighbor_vertex = u.edges[i][0]
        if neighbor_vertex.color == "WHITE":
            dfsVisit(neighbor_vertex, s, visited)
        elif neighbor_vertex.color == "GRAY":
            # Found cycle
            j = len(visited) - 1
            while visited[j] != neighbor_vertex.data: j-=1
            cycle = visited[j:len(visited)]
            cycles.append((cycle, len(cycle)))
            return True

    u.color = "BLACK"
    visited.remove(u.data)
    s.append(u.data)