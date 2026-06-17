
import math 

def binary_search(sorted_arr, target): 

    """Search a SORTED array. O(log n) time, O(1) space.""" 

    low, high = 0, len(sorted_arr) - 1 

    steps = 0 

    while low <= high: 

        steps += 1 

        mid = (low + high) // 2      

        if sorted_arr[mid] == target: 

            print(f'Found in {steps} steps!') 

            return mid 

        elif sorted_arr[mid] < target: 

            low = mid + 1                 

        else: 

            high = mid - 1               

  
    return -1   


data = list(range(0, 1_000_000, 2))  

binary_search(data, 999_998)        


for n in [10, 100, 1000, 1_000_000]: 

    print(f'n={n:>10,}  max steps needed = {math.ceil(math.log2(n))}') 
