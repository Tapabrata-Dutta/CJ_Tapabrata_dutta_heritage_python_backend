# Q5: Compare Merge Sort and Quick Sort for very large datasets

import time
import random

def merge_sort(arr):
    """Merge Sort implementation"""
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def quick_sort(arr):
    """Quick Sort implementation with random pivot"""
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


# Test with large datasets
if __name__ == "__main__":
    sizes = [1000, 5000, 10000]
    
    print("Performance Comparison: Merge Sort vs Quick Sort\n")
    
    for size in sizes:
        data = [random.randint(0, 10000) for _ in range(size)]
        
        # Merge Sort
        start = time.time()
        merge_sort(data.copy())
        merge_time = time.time() - start
        
        # Quick Sort
        start = time.time()
        quick_sort(data.copy())
        quick_time = time.time() - start
        
        print(f"Size: {size} elements")
        print(f"  Merge Sort: {merge_time:.6f}s")
        print(f"  Quick Sort: {quick_time:.6f}s")
        print(f"  Winner: {'Merge Sort' if merge_time < quick_time else 'Quick Sort'}\n")
    
    print("\nConclusion:")
    print("- Merge Sort: O(n log n) guaranteed, consistent, uses extra space")
    print("- Quick Sort: O(n log n) average, faster in practice, in-place sorting")
