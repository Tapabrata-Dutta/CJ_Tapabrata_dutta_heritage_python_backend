correct_pin = '1234'
attempts = 0
max_attempts = 3


while attempts < max_attempts:
    pin = input('Enter PIN: ')
    if pin == correct_pin:
        print('✅ Access Granted!')
        break
    else:
        attempts += 1
        remaining = max_attempts - attempts
        print(f'❌ Wrong PIN. {remaining} attempt(s) left.')
else:
    print('🔒 Card blocked. Too many wrong attempts.')
