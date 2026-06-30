from collections import deque

routes = {
    "Delhi": ["Mumbai", "Kolkata"],
    "Mumbai": ["Goa"],
    "Kolkata": ["Chennai"],
    "Goa": [],
    "Chennai": []
}

start = "Delhi"

queue = deque([start])
visited = set([start])

print("Reachable Destinations:")

while queue:
    city = queue.popleft()
    print(city)

    for neighbour in routes[city]:
        if neighbour not in visited:
            visited.add(neighbour)
            queue.append(neighbour)