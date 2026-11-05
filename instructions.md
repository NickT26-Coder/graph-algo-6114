Steps to test the 3 algorithms:
- In main.py replace "filename.txt" with one of the 15 text files in /graph-txt-files
- Graphs 1 - 5 are for DFS / Topo, graphs 6 - 10 are for Dijkstra's and the last 5 are for Kruskal's
- run python main.py in the terminal and results will be printed in the terminal.
- DFS prints the topological sort if acyclic and the list of cycles with their lengths if not. 
- Dijkstra's returns the shortest path from the given source
- Kruskal's returns the minimum spanning tree with its total path cost