employees = {}

while True:

    print("\n1.Add Employee")
    print("2.Search Employee")
    print("3.Update Employee")
    print("4.Delete Employee")
    print("5.Display Employees")
    print("6.Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        emp_id = input("Enter ID: ")
        name = input("Enter Name: ")
        employees[emp_id] = name

    elif choice == 2:
        emp_id = input("Enter ID: ")

        if emp_id in employees:
            print("Name:", employees[emp_id])
        else:
            print("Employee Not Found")

    elif choice == 3:
        emp_id = input("Enter ID: ")

        if emp_id in employees:
            employees[emp_id] = input("Enter New Name: ")
        else:
            print("Employee Not Found")

    elif choice == 4:
        emp_id = input("Enter ID: ")

        if emp_id in employees:
            del employees[emp_id]
        else:
            print("Employee Not Found")

    elif choice == 5:
        print(employees)

    elif choice == 6:
        break