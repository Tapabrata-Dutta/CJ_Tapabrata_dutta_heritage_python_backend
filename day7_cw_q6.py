num = int(input("Enter a Number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")