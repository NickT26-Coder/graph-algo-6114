'''
Kruskal's Algorithm works by using sets to represents "clouds" of the currently explored graph. The algorithm explores the graph by first sorting the edges of the graph 
by there weights and then selecting the edge with lowest weight at each iteration. You would then add this vertex to a set but, you have two vertices u and v. If u is already 
in the same set as v then you don't add(union) to the set and move onto the next edge. 

Psuedo Code:
Algo kruskalAlgo(g) ->
  total_cost = 0
  MST = []
  sets = []
  for vertex v in graph g ->
    sets.append(set(v))
  edges = sort(edges, w)
  for each edge(u,v) in edges ->
    u_set = FIND-SET(u, sets)
    v_set = FIND-SET(v, sets)
    if u != v ->
      MST.append(edge(u,v))
      total_cost += w
      UNION(u_set, v_set)
      remove v_set from sets
      
  print(MST)
  print(total_cost)

Algo FIND-SET(vertex, sets) ->
  for s in sets:
    if vertex in s:
      return s
    
Runtime:
O(elog(e)), e = number of edges in the graph
The sorting of the edges has the highest time complexity out of all the summative operations.
Check comments in code below

'''
from graph import graphADT

def kruskalAlgo(g: graphADT):
    total_cost = 0
    mst = []
    sets = []

    # O(v), v = number of vertices
    for v in g.vertices:
        s = {v.data}
        sets.append(s)
    # O(elog(e)), uses the quicksort by default
    edges = sorted(g.edges, key= lambda x:x[2])
    # O(e)
    for (u, v, w) in edges:
        # findSet = O(s), s = number of sets, less sets than edges
        u_set = findSet(u.data, sets)
        v_set = findSet(v.data, sets)
        if u_set != v_set:
            mst.append((u.data,v.data))
            total_cost += w
            # O(1), set operations are typically constant since they are built by hash tables
            u_set.update(v_set)
            sets.remove(v_set)

    print(total_cost)
    print(mst)
            

def findSet(v: str, sets: list[set]):
    for s in sets:
        if v in s:
            return s
