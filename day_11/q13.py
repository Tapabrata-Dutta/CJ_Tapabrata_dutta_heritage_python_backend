# Unpack GPS coordinates 

coords = (28.6139, 77.2090) 

latitude, longitude = coords 

print(f'Lat: {latitude}, Lon: {longitude}') 

# Lat: 28.6139, Lon: 77.209 

 

# Unpack student record 

student = ('Bob', 21, 'CSE', 8.5) 

name, age, branch, gpa = student 

print(f'{name} is {age} years old, GPA: {gpa}') 

 

# Unpack in a for loop (very common!) 

employees = [('Alice', 50000), ('Bob', 60000), ('Carol', 55000)] 

for name, salary in employees: 

    print(f'{name} earns ₹{salary:,}') 

 

# Extended unpacking with * (star) 

first, *middle, last = (10, 20, 30, 40, 50) 

print(first)   # 10 

print(middle)  # [20, 30, 40] 

print(last)    # 50 

 

# Ignore values with _ 

name, _, branch, _ = ('Alice', 20, 'CSE', 8.9) 

print(name, branch)  # Alice CSE 