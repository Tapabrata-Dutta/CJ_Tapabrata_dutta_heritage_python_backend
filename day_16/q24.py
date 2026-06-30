graph = {
    1: [2],
    2: [1,3],
    3: [2,4],
    4: [3,2]
}

visited = set()

def dfs(node, parent):
    visited.add(node)

    for neighbour in graph[node]:
        if neighbour not in visited:
            if dfs(neighbour, node):
                return True
        elif neighbour != parent:
            return True

    return False

cycle = False

for node in graph:
    if node not in visited:
        if dfs(node, -1):
            cycle = True
            break

print("Cycle Found" if cycle else "No Cycle")