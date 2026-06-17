list1 = []
list2 = []

for x in input("Enter first list: ").split():
    list1.append(int(x))

for x in input("Enter second list: ").split():
    list2.append(int(x))

merged = list1 + list2
result = []

for i in merged:
    if i not in result:
        result.append(i)

print(result)