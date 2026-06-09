employee_id = input("Enter Employee ID   : ")
password    = input("Enter Password      : ")


# Simulate authentication
if employee_id == "EMP001" and password == "pass123":
    print("Login Successful! Welcome.")
else:
    print("Invalid credentials. Access Denied.")
