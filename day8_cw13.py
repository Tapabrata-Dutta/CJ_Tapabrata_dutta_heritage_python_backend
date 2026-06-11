while True:   # Intentional infinite loop
    print('\n=== MENU ===')
    print('1. Say Hello')
    print('2. Show Date')
    print('3. Quit')
    choice = input('Choose: ')


    if choice == '1':
        print('Hello, World!')
    elif choice == '2':
        from datetime import date
        print('Today:', date.today())
    elif choice == '3':
        print('Goodbye!')
        break
    else:
        print('Invalid choice!')
