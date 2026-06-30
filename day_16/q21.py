graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

visited = set()
stack = ['A']

while stack:
    node = stack.pop()

    if node not in visited:
        print(node, end=" ")
        visited.add(node)

        for neighbour in reversed(graph[node]):
            stack.append(neighbour)