

fruits = ['apple', 'banana', 'cherry', 'date'] 

print(fruits[2])   

  

user_ages = {'Alice': 30, 'Bob': 25, 'Charlie': 35} 

print(user_ages['Bob']) 

  

def sum_of_n(n): 

    return n * (n + 1) // 2   #

  

print(sum_of_n(1_000_000))  

  

# 4. Stack operations 

stack = [] 

stack.append(10)    # O(1) push 

stack.append(20) 

top = stack.pop()   # O(1) pop → returns 20 

