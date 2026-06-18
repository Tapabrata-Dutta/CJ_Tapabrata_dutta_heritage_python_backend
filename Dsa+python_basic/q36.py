numbers = [10, 20, 30, 20, 40, 20, 50]

target = int(input("Enter number to search: "))

for i in range(len(numbers)):
    if numbers[i] == target:
        print("Found at index", i)