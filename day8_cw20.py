print('Multiplication Table (1–5 × 1–5)')
print('+' + '------+' * 5)


# Header row
print('|  × |', end='')
for col in range(1, 6):
    print(f'  {col}  |', end='')
print()
print('+' + '------+' * 5)


# Data rows
for row in range(1, 6):
    print(f'|  {row} |', end='')
    for col in range(1, 6):           # Inner loop
        print(f' {row*col:3d}  |', end='')
    print()
    print('+' + '------+' * 5)
