list1 = []
list2 = []

for x in input("Enter first list: ").split():
    list1.append(int(x))

for x in input("Enter second list: ").split():
    list2.append(int(x))

common = []

for i in list1:
    if i in list2 and i not in common:
        common.append(i)

print(common)