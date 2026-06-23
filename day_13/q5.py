from collections import deque
 
# Social network: adjacency list
network = {
    'Priya':   ['Karan', 'Sunita'],
    'Karan':   ['Priya', 'Rohan', 'Meena'],
    'Sunita':  ['Priya', 'Vikram'],
    'Rohan':   ['Karan'],
    'Meena':   ['Karan', 'Arjun'],
    'Vikram':  ['Sunita', 'Arjun'],
    'Arjun':   ['Meena', 'Vikram'],
}
 
def bfs_shortest_path(graph, start, target):
    """Find the shortest chain between two people using BFS queue."""
    queue   = deque([[start]])     # Queue stores PATHS not just nodes
    visited = {start}
 
    while queue:
        path = queue.popleft()     # FIFO — always explore shortest path
        node = path[-1]
 
        if node == target:
            return path            # Shortest path found!
 
        for friend in graph.get(node, []):
            if friend not in visited:
                visited.add(friend)
                queue.append(path + [friend])  # Extend this path
 
    return None   # No connection found
 
 
# Test: How is Priya connected to Arjun?
path = bfs_shortest_path(network, 'Priya', 'Arjun')
print(f'Connection: {" → ".join(path)}')
print(f'Degrees of separation: {len(path)-1}')
 
path2 = bfs_shortest_path(network, 'Rohan', 'Vikram')
print(f'Connection: {" → ".join(path2)}')
print(f'Degrees of separation: {len(path2)-1}')
