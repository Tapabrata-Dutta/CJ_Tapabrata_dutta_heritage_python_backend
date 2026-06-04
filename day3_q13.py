# 1. Compare marks of two students and print who scored higher

marks1 = int(input("Enter marks of Student 1: "))
marks2 = int(input("Enter marks of Student 2: "))

if marks1 > marks2:
    print("Student 1 scored higher")
elif marks2 > marks1:
    print("Student 2 scored higher")
else:
    print("Both students scored the same")