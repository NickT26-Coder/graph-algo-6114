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
-  
-
-

'''
from graph import graphADT

def kruskalAlgo(g: graphADT):
    total_cost = 0
    mst = []
    sets = []

    for v in g.vertices:
        s = {v.data}
        sets.append(s)
    edges = sorted(g.edges, key= lambda x:x[2])
    for (u, v, w) in edges:
        u_set = findSet(u.data, sets)
        v_set = findSet(v.data, sets)
        if u_set != v_set:
            mst.append((u.data,v.data))
            total_cost += w
            u_set.update(v_set)
            sets.remove(v_set)

    print(total_cost)
    print(mst)
            

def findSet(v: str, sets: list[set]):
    for s in sets:
        if v in s:
            return s
