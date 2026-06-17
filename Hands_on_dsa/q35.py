n = int(input("Enter N: "))

lst = []

for x in input("Enter numbers: ").split():
    lst.append(int(x))

expected_sum = n * (n + 1) // 2
actual_sum = sum(lst)

print("Missing number:", expected_sum - actual_sum)