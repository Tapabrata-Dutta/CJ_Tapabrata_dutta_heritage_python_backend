lst = []

for x in input("Enter elements: ").split():
    lst.append(int(x))

max_element = lst[0]
max_count = lst.count(lst[0])

for i in lst:
    if lst.count(i) > max_count:
        max_count = lst.count(i)
        max_element = i

print("Element:", max_element)
print("Count:", max_count)