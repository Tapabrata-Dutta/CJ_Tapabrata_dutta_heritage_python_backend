list1 = []

n1 = int(input("Enter size of first list: "))

for i in range(n1):
    num = int(input("Enter element: "))
    list1.append(num)

list2 = []

n2 = int(input("\nEnter size of second list: "))

for i in range(n2):
    num = int(input("Enter element: "))
    list2.append(num)

common = sorted(set(list1).intersection(list2))

if common:
    print("Common elements:", common)
else:
    print("No common elements found.")