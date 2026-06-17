
def linear_search(arr, target): 

    """ 

    Search for target in arr. 

    Returns: index if found, -1 if not found. 

    Time:  O(n)   | Space: O(1) 

    """ 

    for index in range(len(arr)):     # visit each element 

        if arr[index] == target:       # found it! 

            return index 

    return -1                          # exhausted all elements 

  

# Test cases 

numbers = [64, 34, 25, 12, 22, 11, 90] 

  

print(linear_search(numbers, 22))   # → 4 (found at index 4) 

print(linear_search(numbers, 100))  # → -1 (not found) 

print(linear_search(numbers, 64))   # → 0 (found at start — best case!) 

print(linear_search(numbers, 90))   # → 6 (found at end — worst case!) 

