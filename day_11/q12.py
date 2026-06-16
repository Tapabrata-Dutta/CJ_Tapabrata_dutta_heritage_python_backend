# Traditional way (other languages) 

a = 10 

b = 20 

temp = a 

a = b 

b = temp 

 

# Pythonic way using tuple unpacking ✨ 

a = 10 

b = 20 

a, b = b, a 

print(a, b)  # 20 10 

 

# Real example: sort two numbers 

x, y = 100, 45 

if x < y: 

    x, y = y, x   # ensure x is always larger 

print(f'Larger: {x}, Smaller: {y}')  # Larger: 100, Smaller: 45 

 

# Swap in sorting algorithms 

arr = [3, 1, 4, 1, 5] 

arr[0], arr[2] = arr[2], arr[0]  # swap index 0 and 2 

print(arr)  # [4, 1, 3, 1, 5] 