membership = 'gold'
purchase_amount = 4500


if membership == 'gold':
    if purchase_amount >= 5000:
        discount = 20
    elif purchase_amount >= 2000:
        discount = 15
    else:
        discount = 10
elif membership == 'silver':
    if purchase_amount >= 3000:
        discount = 10
    else:
        discount = 5
else:
    discount = 0


final = purchase_amount * (1 - discount / 100)
print(f'Discount: {discount}%  |  Final Price: Rs.{final:.2f}')

