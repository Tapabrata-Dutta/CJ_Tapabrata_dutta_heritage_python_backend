import time

graph_list = {
    0:[1,2],
    1:[0,3],
    2:[0],
    3:[1]
}

matrix = [
    [0,1,1,0],
    [1,0,0,1],
    [1,0,0,0],
    [0,1,0,0]
]

# Adjacency List
start = time.time()

visited = set()
stack = [0]

while stack:
    node = stack.pop()

    if node not in visited:
        visited.add(node)

        for neighbour in graph_list[node]:
            stack.append(neighbour)

end = time.time()

print("Adjacency List Time =", end-start)

# Adjacency Matrix
start = time.time()

visited = set()
stack = [0]

while stack:
    node = stack.pop()

    if node not in visited:
        visited.add(node)

        for i in range(len(matrix)):
            if matrix[node][i] == 1:
                stack.append(i)

end = time.time()

print("Adjacency Matrix Time =", end-start)