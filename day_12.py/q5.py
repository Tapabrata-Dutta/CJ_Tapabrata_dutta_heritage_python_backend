def bubble_sort(arr): 

    n = len(arr) 

    comparisons = 0 

    for i in range(n):           

        for j in range(n - i - 1):  

            comparisons += 1 

            if arr[j] > arr[j + 1]: 

                arr[j], arr[j + 1] = arr[j + 1], arr[j] 

    print(f'Comparisons made: {comparisons}') 

    return arr 

  

bubble_sort([5, 3, 8, 1, 9, 2]) 


def find_duplicates(arr): 

    pairs = [] 

    for i in range(len(arr)):         

        for j in range(i + 1, len(arr)):  

            if arr[i] == arr[j]: 

                pairs.append((arr[i], arr[j])) 

    return pairs 


def multiplication_table(n): 

    for i in range(1, n + 1):    # O(n) 

        for j in range(1, n + 1):  # O(n) 

            print(f'{i*j:4}', end='') 

        print() 

