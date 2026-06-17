
import math 

  

def binary_search(sorted_arr, target): 

    """Search a SORTED array. O(log n) time, O(1) space.""" 

    low, high = 0, len(sorted_arr) - 1 

    steps = 0 

  

    while low <= high: 

        steps += 1 

        mid = (low + high) // 2          # find middle index 

  

        if sorted_arr[mid] == target: 

            print(f'Found in {steps} steps!') 

            return mid 

        elif sorted_arr[mid] < target: 

            low = mid + 1                # discard LEFT half 

        else: 

            high = mid - 1               # discard RIGHT half 

  

    return -1   # not found 

  

# Demo 

data = list(range(0, 1_000_000, 2))    # 500,000 even numbers 

binary_search(data, 999_998)           # Found in 19 steps! 

# Linear search would take up to 500,000 steps! 

  

# Power of halving: 

for n in [10, 100, 1000, 1_000_000]: 

    print(f'n={n:>10,}  max steps needed = {math.ceil(math.log2(n))}') 

