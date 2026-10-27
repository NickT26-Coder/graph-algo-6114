from dfs import dfsAlgo
from graph import graphADT

g = graphADT("D")
g.insertVertex("A")
g.insertVertex("B")
g.insertVertex("C")
g.insertVertex("D")
g.insertEdge("A", "A", 1)
g.insertEdge("A", "B", 1)
g.insertEdge("B", "C", 1)
g.insertEdge("C", "D", 1)
g.insertEdge("D", "B", 1)

print(dfsAlgo(g))