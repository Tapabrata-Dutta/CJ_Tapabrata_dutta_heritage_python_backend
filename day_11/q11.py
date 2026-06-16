# Simple iteration 

months = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun') 

for month in months: 

    print(month, end=' ') 

# Jan Feb Mar Apr May Jun 

 

# With enumerate 

for i, month in enumerate(months, start=1): 

    print(f'{i:02d}: {month}') 

 

# Iterating list of tuples (very common with databases) 

db_records = [ 

    (1, 'Alice', 'HR', 55000), 

    (2, 'Bob', 'IT', 70000), 

    (3, 'Carol', 'Finance', 65000) 

] 

print(f'{'ID':<5}{'Name':<10}{'Dept':<10}{'Salary':>10}') 

print('-' * 35) 

for id, name, dept, salary in db_records: 

    print(f'{id:<5}{name:<10}{dept:<10}{salary:>10,}') 