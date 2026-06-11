rows = 5
for i in range(1, rows + 1):        # Outer: row number
    for j in range(1, i + 1):       # Inner: prints i stars
        print('*', end=' ')
    print() 
