balance = 5000


while balance > 0:
    print(f'Current Balance: ₹{balance}')
    amount = int(input('Enter withdrawal amount (0 to exit): '))
    if amount == 0:
        print('Thank you for banking with us!')
        break
    elif amount > balance:
        print('❌ Insufficient funds!')
    else:
        balance -= amount
        print(f'✅ Withdrawn ₹{amount}. Remaining: ₹{balance}')
else:
    print('⚠️  Balance exhausted!')
