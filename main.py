from dfs import dfsAlgo
from graph import graphADT

g = graphADT("D")
g.insertVertex("A")
g.insertVertex("B")
g.insertVertex("C")
g.insertVertex("D")
g.insertVertex("E")
g.insertEdge("A", "B", 1)
g.insertEdge("B", "C", 1)
g.insertEdge("D", "C", 1)
g.insertEdge("D", "E", 1)

print(dfsAlgo(g))