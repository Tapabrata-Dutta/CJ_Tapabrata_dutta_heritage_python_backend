numbers = [10, 20, 30, 40, 50]

target = int(input("Enter number: "))

comparisons = 0

for num in numbers:
    comparisons += 1

    if num == target:
        print("Element found")
        break
else:
    print("Element not found")

print("Comparisons:", comparisons)