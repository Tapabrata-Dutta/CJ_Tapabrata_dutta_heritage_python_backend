def get_user(username):
    db = {'alice': {'password': 'pass123', 'active': True}}
    return db.get(username)  # Returns None if not found


username = 'alice'
password = 'pass123'


user = get_user(username)


# Short-circuit: checks user exists BEFORE accessing user fields
if user and user['active'] and user['password'] == password:
    print('Login successful! Welcome,', username)
else:
    print('Login failed.')

