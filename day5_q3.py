# Restaurant Order System
customer = input("Customer Name : ")
dish1     = input("Item 1        : ")
dish2     = input("Item 2        : ")
dish3     = input("Item 3        : ")


print(f"Order for {customer}: {dish1}, {dish2}, {dish3}")

# Handling Multiple Inputs on One Line
# Use  split()  to collect multiple values from a single input line — common in competitive programming and data entry:
# Collect First and Last name in one go
first, last = input("Enter First and Last Name: ").split()
print(f"Hello, {first} {last}!")


# Collect 3 numbers separated by space
a, b, c = input("Enter 3 numbers: ").split()
print("You entered:", a, b, c)
