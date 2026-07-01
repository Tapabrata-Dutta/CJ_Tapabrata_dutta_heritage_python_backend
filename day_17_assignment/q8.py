# Q8: Compare Bubble, Selection, Insertion, Merge, and Quick Sort on 100 random numbers

import time
import random

def bubble_sort(arr):
    """Bubble Sort"""
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def selection_sort(arr):
    """Selection Sort"""
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def insertion_sort(arr):
    """Insertion Sort"""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def merge_sort(arr):
    """Merge Sort"""
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    """Merge for Merge Sort"""
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
    """Quick Sort"""
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


if __name__ == "__main__":
    # Generate 100 random numbers
    data = [random.randint(0, 1000) for _ in range(100)]
    
    algorithms = [
        ("Bubble Sort", bubble_sort),
        ("Selection Sort", selection_sort),
        ("Insertion Sort", insertion_sort),
        ("Merge Sort", merge_sort),
        ("Quick Sort", quick_sort)
    ]
    
    print("Sorting Algorithm Comparison (100 random numbers)")
    print("="*60)
    print(f"{'Algorithm':<20} {'Time (seconds)':<20} {'Complexity'}")
    print("-"*60)
    
    results = []
    
    for name, algo in algorithms:
        start = time.time()
        result = algo(data.copy())
        elapsed = time.time() - start
        
        # Determine complexity
        if name == "Bubble Sort" or name == "Selection Sort":
            complexity = "O(n²)"
        elif name == "Insertion Sort":
            complexity = "O(n²)"
        else:
            complexity = "O(n log n)"
        
        print(f"{name:<20} {elapsed:<20.8f} {complexity}")
        results.append((name, elapsed))
    
    print("="*60)
    print("\nConclusion:")
    print("- Simple sorts (Bubble, Selection, Insertion) are O(n²)")
    print("- Advanced sorts (Merge, Quick) are O(n log n)")
    print("- For 100 elements, Merge and Quick sort are significantly faster")
