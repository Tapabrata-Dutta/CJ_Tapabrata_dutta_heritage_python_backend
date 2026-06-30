graph = {
    1: [2],
    2: [1],
    3: [4],
    4: [3],
    5: []
}

visited = set()
count = 0

def dfs(node):
    stack = [node]

    while stack:
        x = stack.pop()

        if x not in visited:
            visited.add(x)

            for neighbour in graph[x]:
                stack.append(neighbour)

for node in graph:
    if node not in visited:
        count += 1
        dfs(node)

print("Connected Components =", count)