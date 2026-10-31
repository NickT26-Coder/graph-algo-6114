class graphADT:
    class vertex:
        def __init__(self, data: str):
            self.data = data
            self.color = "WHITE"
            self.edges = []
        
    def __init__(self, type: str):
        self.type = type
        self.vertices = []
        self.edges = []

    def __str__(self):
        result = ""
        for vertex in self.vertices:
            result += vertex.data + "\n"

        return result

    def findVertex(self, v: str) -> vertex | None:
        for vertex in self.vertices:
            if vertex.data == v:
                return vertex
        return None

    def insertVertex(self, v: str) -> None:
        self.vertices.append(self.vertex(v))

    def insertEdge(self, u: str, v: str, weight: int) -> None:
        u = self.findVertex(u)
        v = self.findVertex(v)

        self.edges.append((u, v, weight))
        if (v, weight) not in u.edges:
            if self.type == "D":
                u.edges.append((v, weight))
            else:
                u.edges.append((v, weight))
                v.edges.append((u, weight))