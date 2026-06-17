emp_ids = [101, 102, 103, 104, 203, 210, 214, 214]
emp_names = ["Rahul", "Priya", "Amit", "Sneha", "Bikram", "Yash", "Aryan", "keya"]

search_id = int(input("Enter Employee ID: "))

for i in range(len(emp_ids)):
    if emp_ids[i] == search_id:
        print("Employee Found")
        print("ID:", emp_ids[i])
        print("Name:", emp_names[i])
        break
else:
    print("Employee Not Found")