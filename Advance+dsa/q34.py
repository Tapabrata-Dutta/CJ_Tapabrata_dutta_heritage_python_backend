list1 = [10, 20, 30, 40]
list2 = [20, 30, 50, 60]
list3 = [30, 20, 70, 80]

common = set(list1) & set(list2) & set(list3)

print("Common Elements:", common)