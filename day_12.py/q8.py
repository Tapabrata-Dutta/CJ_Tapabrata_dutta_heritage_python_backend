
def linear_search(arr, target): 

    """ 

    Search for target in arr. 

    Returns: index if found, -1 if not found. 

    Time:  O(n)   | Space: O(1) 

    """ 

    for index in range(len(arr)):     

        if arr[index] == target:       

            return index 

    return -1                    

numbers = [64, 34, 25, 12, 22, 11, 90] 

  

print(linear_search(numbers, 22))   

print(linear_search(numbers, 100))  

print(linear_search(numbers, 64))   

print(linear_search(numbers, 90))    

