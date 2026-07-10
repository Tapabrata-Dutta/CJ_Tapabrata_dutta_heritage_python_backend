"""
q3_sorting.py
This script implements five sorting algorithms from scratch (Bubble, Selection, Insertion, Merge, Quick Sort)
with detailed trace outputs and time complexity annotations.
"""

def bubble_sort(arr):
    """
    Bubble Sort Implementation.
    Compares adjacent elements and swaps them if they are in the wrong order.
    
    Time Complexity:
    - Best Case: O(n)       -> When the list is already sorted (using the optimized swap check).
    - Average Case: O(n^2)  -> Typical random order list.
    - Worst Case: O(n^2)    -> When the list is sorted in reverse order.
    
    Space Complexity: O(1)  -> In-place sorting.
    """
    temp = arr.copy()
    n = len(temp)
    print(f"Initial: {temp}")
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if temp[j] > temp[j + 1]:
                temp[j], temp[j + 1] = temp[j + 1], temp[j]
                swapped = True
        print(f"Pass {i+1}: {temp}")
        if not swapped:
            print("No swaps occurred. Early termination.")
            break
    return temp

def selection_sort(arr):
    """
    Selection Sort Implementation.
    Repeatedly finds the minimum element from the unsorted part and puts it at the beginning.
    
    Time Complexity:
    - Best Case: O(n^2)      -> Must scan the remaining unsorted part even if already sorted.
    - Average Case: O(n^2)   -> Standard scanning logic.
    - Worst Case: O(n^2)     -> Same as above.
    
    Space Complexity: O(1)   -> In-place sorting.
    """
    temp = arr.copy()
    n = len(temp)
    print(f"Initial: {temp}")
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if temp[j] < temp[min_idx]:
                min_idx = j
        temp[i], temp[min_idx] = temp[min_idx], temp[i]
        print(f"Pass {i+1} (swapped index {i} and {min_idx}): {temp}")
    return temp

def insertion_sort(arr):
    """
    Insertion Sort Implementation.
    Builds the final sorted array one element at a time by inserting each new element into its proper position.
    
    Time Complexity:
    - Best Case: O(n)        -> When the list is already sorted (only 1 comparison per element, no shifts).
    - Average Case: O(n^2)   -> On average, each element is shifted halfway back.
    - Worst Case: O(n^2)     -> When the list is sorted in reverse order (maximum shifts).
    
    Space Complexity: O(1)   -> In-place sorting.
    """
    temp = arr.copy()
    n = len(temp)
    print(f"Initial: {temp}")
    for i in range(1, n):
        key = temp[i]
        j = i - 1
        while j >= 0 and temp[j] > key:
            temp[j + 1] = temp[j]
            j -= 1
        temp[j + 1] = key
        print(f"Step {i} (inserted {key}): {temp}")
    return temp

def merge_sort(arr):
    """
    Merge Sort Implementation (Recursive).
    A divide-and-conquer algorithm that splits the array into halves, sorts them, and merges them.
    
    Time Complexity:
    - Best Case: O(n log n)    -> The splitting and merging costs are independent of initial order.
    - Average Case: O(n log n) -> Standard performance.
    - Worst Case: O(n log n)   -> Standard performance.
    
    Space Complexity: O(n)     -> Requires temporary arrays for merging.
    """
    temp = arr.copy()
    
    def merge_sort_recursive(lst, depth=0):
        if len(lst) <= 1:
            return lst
        
        mid = len(lst) // 2
        left = merge_sort_recursive(lst[:mid], depth + 1)
        right = merge_sort_recursive(lst[mid:], depth + 1)
        
        # Merge operation
        merged = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        merged.extend(left[i:])
        merged.extend(right[j:])
        
        print("  " * depth + f"Merged: {left} and {right} -> {merged}")
        return merged

    print(f"Initial: {temp}")
    sorted_arr = merge_sort_recursive(temp)
    return sorted_arr

def quick_sort(arr):
    """
    Quick Sort Implementation (Recursive Partitioning).
    Picks a pivot, and partitions the array into elements smaller, equal, and larger than the pivot.
    
    Time Complexity:
    - Best Case: O(n log n)    -> Balanced partition where pivot is always the median element.
    - Average Case: O(n log n) -> Typically balanced partitions.
    - Worst Case: O(n^2)      -> Highly unbalanced partitioning (e.g. pivot is always minimum/maximum).
    
    Space Complexity: O(log n) -> Call stack depth in average case, O(n) in worst case.
    """
    temp = arr.copy()
    
    def quick_sort_recursive(lst, depth=0):
        if len(lst) <= 1:
            return lst
        
        pivot = lst[len(lst) // 2]
        left = [x for x in lst if x < pivot]
        middle = [x for x in lst if x == pivot]
        right = [x for x in lst if x > pivot]
        
        print("  " * depth + f"Partition (Pivot={pivot}): Left={left}, Mid={middle}, Right={right}")
        
        return quick_sort_recursive(left, depth + 1) + middle + quick_sort_recursive(right, depth + 1)
        
    print(f"Initial: {temp}")
    sorted_arr = quick_sort_recursive(temp)
    print(f"Final Sorted Output: {sorted_arr}")
    return sorted_arr

def main():
    # Sample unsorted list of 8 elements
    sample_list = [29, 10, 14, 37, 13, 2, 8, 25]
    print(f"--- Original Sample List (Length {len(sample_list)}): {sample_list} ---")
    
    results = {}
    
    print("\n==============================================")
    print("                1. BUBBLE SORT                ")
    print("==============================================")
    results['Bubble Sort'] = bubble_sort(sample_list)
    
    print("\n==============================================")
    print("               2. SELECTION SORT              ")
    print("==============================================")
    results['Selection Sort'] = selection_sort(sample_list)
    
    print("\n==============================================")
    print("               3. INSERTION SORT              ")
    print("==============================================")
    results['Insertion Sort'] = insertion_sort(sample_list)
    
    print("\n==============================================")
    print("                 4. MERGE SORT                ")
    print("==============================================")
    results['Merge Sort'] = merge_sort(sample_list)
    
    print("\n==============================================")
    print("                 5. QUICK SORT                ")
    print("==============================================")
    results['Quick Sort'] = quick_sort(sample_list)
    
    print("\n==============================================")
    print("                VERIFICATION                  ")
    print("==============================================")
    
    expected_sorted = sorted(sample_list)
    all_correct = True
    for name, result in results.items():
        correct = (result == expected_sorted)
        print(f"{name:15} | Correct? {correct} | Result: {result}")
        if not correct:
            all_correct = False
            
    if all_correct:
        print("\n[SUCCESS] All 5 sorting algorithms produced the same correctly sorted list!")
    else:
        print("\n[FAILURE] One or more sorting algorithms failed to sort the list correctly.")

if __name__ == "__main__":
    main()

"""
tapabratadutta@TAPABRATAs-MacBook-Air Intern_program % python3 /Users/tapabratadutta/Intern_program/final_revolution/q3_sorting.py
--- Original Sample List (Length 8): [29, 10, 14, 37, 13, 2, 8, 25] ---

==============================================
                1. BUBBLE SORT                
==============================================
Initial: [29, 10, 14, 37, 13, 2, 8, 25]
Pass 1: [10, 14, 29, 13, 2, 8, 25, 37]
Pass 2: [10, 14, 13, 2, 8, 25, 29, 37]
Pass 3: [10, 13, 2, 8, 14, 25, 29, 37]
Pass 4: [10, 2, 8, 13, 14, 25, 29, 37]
Pass 5: [2, 8, 10, 13, 14, 25, 29, 37]
Pass 6: [2, 8, 10, 13, 14, 25, 29, 37]
No swaps occurred. Early termination.

==============================================
               2. SELECTION SORT              
==============================================
Initial: [29, 10, 14, 37, 13, 2, 8, 25]
Pass 1 (swapped index 0 and 5): [2, 10, 14, 37, 13, 29, 8, 25]
Pass 2 (swapped index 1 and 6): [2, 8, 14, 37, 13, 29, 10, 25]
Pass 3 (swapped index 2 and 6): [2, 8, 10, 37, 13, 29, 14, 25]
Pass 4 (swapped index 3 and 4): [2, 8, 10, 13, 37, 29, 14, 25]
Pass 5 (swapped index 4 and 6): [2, 8, 10, 13, 14, 29, 37, 25]
Pass 6 (swapped index 5 and 7): [2, 8, 10, 13, 14, 25, 37, 29]
Pass 7 (swapped index 6 and 7): [2, 8, 10, 13, 14, 25, 29, 37]

==============================================
               3. INSERTION SORT              
==============================================
Initial: [29, 10, 14, 37, 13, 2, 8, 25]
Step 1 (inserted 10): [10, 29, 14, 37, 13, 2, 8, 25]
Step 2 (inserted 14): [10, 14, 29, 37, 13, 2, 8, 25]
Step 3 (inserted 37): [10, 14, 29, 37, 13, 2, 8, 25]
Step 4 (inserted 13): [10, 13, 14, 29, 37, 2, 8, 25]
Step 5 (inserted 2): [2, 10, 13, 14, 29, 37, 8, 25]
Step 6 (inserted 8): [2, 8, 10, 13, 14, 29, 37, 25]
Step 7 (inserted 25): [2, 8, 10, 13, 14, 25, 29, 37]

==============================================
                 4. MERGE SORT                
==============================================
Initial: [29, 10, 14, 37, 13, 2, 8, 25]
    Merged: [29] and [10] -> [10, 29]
    Merged: [14] and [37] -> [14, 37]
  Merged: [10, 29] and [14, 37] -> [10, 14, 29, 37]
    Merged: [13] and [2] -> [2, 13]
    Merged: [8] and [25] -> [8, 25]
  Merged: [2, 13] and [8, 25] -> [2, 8, 13, 25]
Merged: [10, 14, 29, 37] and [2, 8, 13, 25] -> [2, 8, 10, 13, 14, 25, 29, 37]

==============================================
                 5. QUICK SORT                
==============================================
Initial: [29, 10, 14, 37, 13, 2, 8, 25]
Partition (Pivot=13): Left=[10, 2, 8], Mid=[13], Right=[29, 14, 37, 25]
  Partition (Pivot=2): Left=[], Mid=[2], Right=[10, 8]
    Partition (Pivot=8): Left=[], Mid=[8], Right=[10]
  Partition (Pivot=37): Left=[29, 14, 25], Mid=[37], Right=[]
    Partition (Pivot=14): Left=[], Mid=[14], Right=[29, 25]
      Partition (Pivot=25): Left=[], Mid=[25], Right=[29]
Final Sorted Output: [2, 8, 10, 13, 14, 25, 29, 37]

==============================================
                VERIFICATION                  
==============================================
Bubble Sort     | Correct? True | Result: [2, 8, 10, 13, 14, 25, 29, 37]
Selection Sort  | Correct? True | Result: [2, 8, 10, 13, 14, 25, 29, 37]
Insertion Sort  | Correct? True | Result: [2, 8, 10, 13, 14, 25, 29, 37]
Merge Sort      | Correct? True | Result: [2, 8, 10, 13, 14, 25, 29, 37]
Quick Sort      | Correct? True | Result: [2, 8, 10, 13, 14, 25, 29, 37]

[SUCCESS] All 5 sorting algorithms produced the same correctly sorted list!
"""