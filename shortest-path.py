'''
Dijkstra's Algorithm

Dijkstra's algorithm works by initializing the source vertex to a distance and all other vertices with a distance 
of positive infinity. These distances represent the shortest known path to that vertex.

From the current vertex update the distance of the neighboring vertices based on the weight of the edge connecting
the two if it is smaller than the current distance. The distance is calculated by adding the weight of the edge and
the distance of the current node that is searching. In order to keep track of the shortest path from the source 
vertex to every other vertex in the graph we need to add a reference to every vertex that points back to the vertex
that explored it and then backtrack and add to a list to print. 

After updating the current distances to each neighboring vertice we explore the edge with the lowest weight. A min
heap is useful for this process.

Once we find the target we know that we've found the shortest path since we have established the shortest path 
up until that point. 

Psuedo Code:

Algo dijkstras(Graph g, Source_Val s)
    dist = {}
    prev = {}
    heap = []
    s = findVertex(s)
    for each vertex v  in g:
        dist[v] = infinity
        prev[v] = None  
        insert_to_heap(heap, (v, dist[v]))
    dist[s] = 0
    insert_to_heap(heap, (s, dist[s]))
    while heap:
        u = remove_min(heap)
        for each edge(u, v, w) of u:
            if dist[v] > dist[u] + w
                dist[v] = dist[u] + w
                prev[v] = u
    
    # Display Paths
    for each vertex v in g:
        path = [v]
        path_cost = 0
        p = prev[v]
        while p != s:
            path.append(p)
            p = prev[p]
        path.append(s)
        print(path)
        print(dist[v])


Runtime:

'''