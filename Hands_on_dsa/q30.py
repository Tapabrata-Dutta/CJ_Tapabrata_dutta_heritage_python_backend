check = []
for x in input("Enter elements: ").split():
    check.append(int(x))

for i in check:
    if check.count(i) == 1:
        print("The repeating elements is: ", i)
        break
    else:
        "No non repeating elements found"