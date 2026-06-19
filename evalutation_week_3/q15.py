student = {}

name = input("Enter Student Name: ")

num_subjects = int(input("Enter number of subjects: "))
marks = []

for i in range(num_subjects):
    mark = int(input(f"Enter Marks of Subject {i+1}: "))
    marks.append(mark)

total = sum(marks)
average = total / len(marks)

if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
else:
    grade = "F"

student["Name"] = name
student["Marks"] = marks
student["Total"] = total
student["Average"] = average
student["Grade"] = grade

print("\nStudent Result")
for key, value in student.items():
    print(key, ":", value)