from dfs import dfsAlgo
from graph import graphADT

g = graphADT("D")
g.insertVertex("A")
g.insertVertex("B")
g.insertVertex("C")
g.insertVertex("D")
g.insertVertex("E")
g.insertVertex("F")
g.insertEdge("A", "B", 1)
g.insertEdge("A", "C", 1)
g.insertEdge("B", "C", 1)
g.insertEdge("B", "D", 3)
g.insertEdge("B", "E", 2)
g.insertEdge("C", "D", 1)
g.insertEdge("C", "E", 2)
g.insertEdge("D", "E", 4)
g.insertEdge("D", "F", 1)
g.insertEdge("E", "F", 1)

dfsAlgo(g)