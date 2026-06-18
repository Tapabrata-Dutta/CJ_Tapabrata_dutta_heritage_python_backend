cache = {}
capacity = 3

cache["A"] = 1
cache["B"] = 2
cache["C"] = 3

print(cache)

cache.pop("A")
cache["A"] = 1

cache["D"] = 4

if len(cache) > capacity:
    first_key = list(cache.keys())[0]
    del cache[first_key]

print(cache)