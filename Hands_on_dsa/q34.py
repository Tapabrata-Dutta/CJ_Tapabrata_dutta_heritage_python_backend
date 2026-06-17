lst = []

for x in input("Enter elements: ").split():
    lst.append(int(x))

k = int(input("Enter K: "))

k = k % len(lst)

rotated = lst[-k:] + lst[:-k]

print(rotated)