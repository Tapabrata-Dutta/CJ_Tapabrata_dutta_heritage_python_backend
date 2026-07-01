# Q7: Show a case where Quick Sort performs poorly

import time

def quick_sort_worst_case(arr, low=0, high=None):
    """
    Quick Sort with first element as pivot (can lead to worst case).
    """
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        pivot_index = partition_first(arr, low, high)
        quick_sort_worst_case(arr, low, pivot_index - 1)
        quick_sort_worst_case(arr, pivot_index + 1, high)
    
    return arr

def partition_first(arr, low, high):
    """Partition with first element as pivot"""
    pivot = arr[low]
    i = low + 1
    
    for j in range(low + 1, high + 1):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    
    arr[low], arr[i - 1] = arr[i - 1], arr[low]
    return i - 1


print("Quick Sort Worst Case Scenario\n")
print("="*50)

# Case 1: Already sorted array (worst case for first/last pivot)
sorted_array = list(range(1000))
print("\nCase 1: Already Sorted Array (1000 elements)")
print("Pivot selection: First element")
print("Expected behavior: Creates unbalanced partitions")

start = time.time()
quick_sort_worst_case(sorted_array.copy())
worst_case_time = time.time() - start

print(f"Time taken: {worst_case_time:.6f}s")
print("Time Complexity: O(n²) instead of O(n log n)")

# Case 2: Reverse sorted array
reverse_sorted = list(range(999, -1, -1))
print("\nCase 2: Reverse Sorted Array (1000 elements)")
print("This also causes O(n²) behavior")

start = time.time()
quick_sort_worst_case(reverse_sorted.copy())
worst_case_time2 = time.time() - start

print(f"Time taken: {worst_case_time2:.6f}s")

print("\n" + "="*50)
print("\nWhy Quick Sort performs poorly:")
print("1. Bad pivot selection → unbalanced partitions")
print("2. Unbalanced partitions → deep recursion")
print("3. Deep recursion → O(n²) time complexity")
print("\nSolution: Use random pivot selection or median-of-three")
