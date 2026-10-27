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

DFS(g) ->
create a stack
create a list of visited nodes
for each vertex v in g ->
    if v.color == White
        dfsVisit(v, s, visited)

if cycle exists ->
    return list of cycles
else ->
    return reverse s

dfsVisit(v, s, visited) ->
    v.color = Gray
    visited.append(v.data)
    for i in v.edges ->
        neighbor_vertex = v.edges[0]
        if neighbor_vertex = White ->
            dfsVisit(neighbor_vertex, s, visited)
        elif neightbor_vertex = Gray ->
            obtain cycle as a new list
            append cycle to list of cycles
            return True

    v.color = Black
    v.remove(v.data), remove finished node
    s.append(v.data), add to recursive stack

Runtime:
Total = O(V + E)
Runtime explained in comments in code below

'''

# Implementation
from graph import graphADT

cycles = []

def dfsAlgo(g: graphADT):
    s = []
    visited = []
    # O(v), visits each vertex in the graph once
    for vertex in g.vertices:
        if vertex.color == "WHITE":
            dfsVisit(vertex, s, visited)

    if len(cycles) > 0:
        return cycles
    else:
        topo = []
        # O(v), the stack is the same size as the number of vertices, only executes on acyclic graphs
        while s:
            topo.append(s.pop())

        return topo

def dfsVisit(u: graphADT.vertex, s: list[str], visited: list[str]):
    u.color = "GRAY"
    visited.append(u.data)
    # O(E), visits each neighboring vertex and there subsequent neighboring vertices which are connected by an edge
    for i in range(len(u.edges)):
        neighbor_vertex = u.edges[i][0]
        if neighbor_vertex.color == "WHITE":
            dfsVisit(neighbor_vertex, s, visited)
        elif neighbor_vertex.color == "GRAY":
            # Found cycle
            j = len(visited) - 1
            # O(v), loops back to a previous instance of the same node to create a cycle list
            while visited[j] != neighbor_vertex.data: j-=1
            cycle = visited[j:len(visited)]
            cycles.append((cycle, len(cycle)))
            return True

    u.color = "BLACK"
    visited.remove(u.data)
    s.append(u.data)