from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': []
}

start = 'A'
end = 'E'

queue = deque([start])
visited = set([start])

found = False

while queue:
    node = queue.popleft()

    if node == end:
        found = True
        break

    for neighbour in graph[node]:
        if neighbour not in visited:
            visited.add(neighbour)
            queue.append(neighbour)

print("Path Exists" if found else "No Path")