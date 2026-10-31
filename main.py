from dfs import dfsAlgo
from graph import graphADT


def createGraphFromFile(filename: str) -> graphADT:
    values = {}
    with open(f"graph-txt-files/{filename}", 'r') as f:
        header = f.readline().strip().split(" ")
        g = graphADT(type=header[2])
        for row in f:
            data = row.strip().split(" ")
            u, v, w = data[0], data[1], data[2]
            if not values.get(u):
                values[u] = True
                g.insertVertex(u)
            if not values.get(v):
                values[v] = True
                g.insertVertex(v)

            g.insertEdge(u, v, w)

    return g
            

g = createGraphFromFile("graph-ex.txt")

print(dfsAlgo(g))