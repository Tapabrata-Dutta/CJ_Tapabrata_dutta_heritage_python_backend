from collections import deque

graph = {
    0: [1],
    1: [0,2],
    2: [1,3],
    3: []
}

start = 0
goal = 3

queue = deque([(start,[start])])
visited = set()

while queue:
    node, path = queue.popleft()

    if node == goal:
        print("Path:", path)
        break

    if node not in visited:
        visited.add(node)

        for neighbour in graph[node]:
            queue.append((neighbour, path+[neighbour]))