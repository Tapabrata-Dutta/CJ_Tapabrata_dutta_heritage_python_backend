salary = float(input("Enter Current Salary: "))
increment_percent = float(input("Enter Increment Percentage: "))

increment_amount = (salary * increment_percent) / 100
revised_salary = salary + increment_amount

print("Revised Salary =", revised_salary)