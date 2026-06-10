def validate_form(name, email, age):
# Short-circuit: stops at first failure
    if not name or not email or not age:
        return 'Error: All fields are required'


    if not '@' in email or not '.' in email:
        return 'Error: Invalid email format'


    if not age.isdigit() or not (1 <= int(age) <= 120):
        return 'Error: Age must be between 1 and 120'


    return 'Form submitted successfully!'


print(validate_form('Rahul', 'rahul@email.com', '25'))
print(validate_form('', 'test@test.com', '30'))
print(validate_form('Priya', 'invalidemail', '22'))

