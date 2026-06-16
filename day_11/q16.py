employees = ['Alice', 'Bob', 'Carol'] 

 

# New employee joins 

employees.append('David') 

employees.append('Eva') 

 

print(employees) 

# ['Alice', 'Bob', 'Carol', 'David', 'Eva'] 

 

# append() adds ONE item at a time 

# To add multiple items, use extend() 

employees.extend(['Frank', 'Grace']) 

print(employees) 

# ['Alice', 'Bob', 'Carol', 'David', 'Eva', 'Frank', 'Grace'] 