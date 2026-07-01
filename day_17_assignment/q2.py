# Q2: Explain why Insertion Sort is efficient for nearly sorted data

"""
Why Insertion Sort is Efficient for Nearly Sorted Data:

1. **Adaptive Nature**: Insertion Sort's time complexity depends on the number of inversions 
   (pairs of elements out of order) in the array.
   - Best case: O(n) when array is already sorted
   - Average case: O(n²) for random data
   - Worst case: O(n²) when array is reverse sorted

2. **Nearly Sorted Arrays**: For nearly sorted data with few inversions, each element needs 
   minimal movement, making Insertion Sort very efficient.

3. **Number of Comparisons**: Proportional to inversions, not array size.

4. **Practical Performance**: Often outperforms O(n log n) algorithms (like QuickSort, MergeSort) 
   on small or nearly sorted datasets due to lower overhead.

5. **Space Efficiency**: Uses O(1) extra space (in-place sorting).
"""

import time

def insertion_sort(arr):
    """Insertion Sort implementation"""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Example: Nearly sorted data is much faster
nearly_sorted = list(range(1000)) + [999, 998, 997]  # Almost sorted
random_data = [500, 200, 800, 100, 900] * 200  # Random data

print("Testing Insertion Sort on nearly sorted data vs random data...")

start = time.time()
insertion_sort(nearly_sorted.copy())
nearly_time = time.time() - start

start = time.time()
insertion_sort(random_data.copy())
random_time = time.time() - start

print(f"Nearly sorted time: {nearly_time:.6f}s")
print(f"Random data time: {random_time:.6f}s")
print(f"Nearly sorted is {random_time/nearly_time:.2f}x faster!")
