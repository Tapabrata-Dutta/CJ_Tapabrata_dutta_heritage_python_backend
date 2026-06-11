limit = 1000
a, b = 0, 1


print('Fibonacci sequence up to', limit)
while a <= limit:
    print(a, end=' ')
    a, b = b, a + b    # Swap and add


print()
