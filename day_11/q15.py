queue = ['Task1', 'Task2', 'Task3', 'Task4'] 

 

# Remove last item (stack behavior) 

last = queue.pop() 

print(last)   # Task4 

print(queue)  # ['Task1', 'Task2', 'Task3'] 

 

# Remove specific index 

first = queue.pop(0)   # FIFO behavior 

print(first)  # Task1 

print(queue)  # ['Task2', 'Task3'] 