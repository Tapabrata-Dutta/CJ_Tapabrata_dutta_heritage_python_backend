class Vertex:
    def __init__(self, data):
        self.data = data
        self.neighbours = []

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, data):
        self.vertices[data] = Vertex(data)

    def add_edge(self, u, v):
        self.vertices[u].neighbours.append(v)
        self.vertices[v].neighbours.append(u)

    def dfs(self, start):
        visited = set()
        stack = [start]

        while stack:
            node = stack.pop()

            if node not in visited:
                print(node, end=" ")
                visited.add(node)

                for neighbour in self.vertices[node].neighbours:
                    stack.append(neighbour)

g = Graph()

for i in ['A','B','C','D']:
    g.add_vertex(i)

g.add_edge('A','B')
g.add_edge('A','C')
g.add_edge('B','D')

g.dfs('A')