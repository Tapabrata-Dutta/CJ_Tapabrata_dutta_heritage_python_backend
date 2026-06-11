employee = {
    'name': 'Ravi Kumar',
    'role': 'Developer',
    'salary': 75000
}


# Iterate over keys
for key in employee:
    print(f'{key}: {employee[key]}')


# Iterate over key-value pairs
for key, value in employee.items():
    print(f'{key.upper()} => {value}')
