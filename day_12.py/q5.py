def bubble_sort(arr): 

    n = len(arr) 

    comparisons = 0 

    for i in range(n):           # outer loop: n times 

        for j in range(n - i - 1):  # inner loop: ~n times 

            comparisons += 1 

            if arr[j] > arr[j + 1]: 

                arr[j], arr[j + 1] = arr[j + 1], arr[j] 

    print(f'Comparisons made: {comparisons}') 

    return arr 

  

bubble_sort([5, 3, 8, 1, 9, 2]) 

# Comparisons made: 15  (for n=6, n²/2 ≈ 18) 

  

# 2. Finding all duplicate pairs 

def find_duplicates(arr): 

    pairs = [] 

    for i in range(len(arr)):         # O(n) 

        for j in range(i + 1, len(arr)):  # O(n) 

            if arr[i] == arr[j]: 

                pairs.append((arr[i], arr[j])) 

    return pairs 

  

# 3. Multiplication table 

def multiplication_table(n): 

    for i in range(1, n + 1):    # O(n) 

        for j in range(1, n + 1):  # O(n) 

            print(f'{i*j:4}', end='') 

        print() 

