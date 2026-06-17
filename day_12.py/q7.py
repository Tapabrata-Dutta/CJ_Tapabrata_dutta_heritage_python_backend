
import bisect 

  

def example_c(arr, queries): 

    sorted_arr = sorted(arr)         

    for q in queries:                 # O(q) — q queries 

        # bisect uses binary search internally → O(log n) 

        idx = bisect.bisect_left(sorted_arr, q)   # O(log n) 

        print(idx) 

