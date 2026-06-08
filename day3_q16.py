# 4. Check if a user is eligible for voting

age = int(input("Enter age: "))
citizenship = input("Enter citizenship: ")

if age >= 18 and citizenship == "Indian":
    print("Eligible for voting")
else:
    print("Not eligible for voting")