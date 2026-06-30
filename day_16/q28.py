from collections import deque

graph = {
    1:[2,3],
    2:[1,4,5],
    3:[1],
    4:[2],
    5:[2]
}

source = 1
k = 2

queue = deque([(source,0)])
visited = set([source])

while queue:
    node, dist = queue.popleft()

    if dist == k:
        print(node)

    if dist < k:
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append((neighbour, dist+1))