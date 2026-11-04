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
  for each edge(u,v) in g
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
