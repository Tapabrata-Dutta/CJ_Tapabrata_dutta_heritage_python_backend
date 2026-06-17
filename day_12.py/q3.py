
# 1. Finding the maximum value (no built-in) 

def find_max(arr): 

    max_val = arr[0] 

    for num in arr:          # visits every element once → O(n) 

        if num > max_val: 

            max_val = num 

    return max_val 

  

# 2. Counting occurrences 

def count_even(arr): 

    count = 0 

    for num in arr:          # O(n) 

        if num % 2 == 0: 

            count += 1 

    return count 

  

# 3. Copying an array 

def copy_list(arr): 

    result = [] 

    for item in arr:         # O(n) time, O(n) space 

        result.append(item) 

    return result 

  

# 4. Real-life: Reading a 1000-page book 

#    You must visit every page → O(n) where n = pages 

def read_book(pages): 

    for page in pages:       # No shortcut — must read each 

        process(page) 

