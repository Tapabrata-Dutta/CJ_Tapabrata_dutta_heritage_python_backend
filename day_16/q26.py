graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D", "E"],
    "D": ["B", "C"],
    "E": ["C"]
}

user = "A"

friends = set(graph[user])
recommend = set()

for friend in friends:
    for person in graph[friend]:
        if person != user and person not in friends:
            recommend.add(person)

print("Recommendations:", recommend)