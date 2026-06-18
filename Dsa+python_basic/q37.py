employees = {
    101: "Rahul",
    102: "Priya",
    103: "Amit"
}

emp_id = int(input("Enter Employee ID: "))

if emp_id in employees:
    print("Employee Name:", employees[emp_id])
else:
    print("Employee ID not found")