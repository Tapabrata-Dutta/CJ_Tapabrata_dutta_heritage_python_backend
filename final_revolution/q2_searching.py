"""
q2_searching.py
This script implements and compares Linear Search and Binary Search algorithms.
It includes tests on a sample list of at least 10 elements and documents Big-O complexity.
"""

def linear_search(arr, target):
    """
    Performs a linear search to find the target element in an unsorted list.
    
    Time Complexity:
    - Best Case: O(1)       -> Target is the very first element of the list.
    - Average Case: O(n)    -> Target is somewhere in the middle (requires n/2 comparisons on average).
    - Worst Case: O(n)      -> Target is the last element or not present in the list (requires checking all elements).
    
    Space Complexity: O(1)  -> Only constant extra space is used.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    """
    Performs an iterative binary search to find the target element in a sorted list.
    
    Time Complexity:
    - Best Case: O(1)       -> Target is the middle element in the first division.
    - Average Case: O(log n)-> The search space is halved in each step.
    - Worst Case: O(log n)  -> The target is at the end of the search space or not present.
    
    Space Complexity: O(1)  -> Constant extra space is used since it is implemented iteratively.
    
    Why does Binary Search require a sorted array?
    Binary search relies on a divide-and-conquer strategy. It compares the target value to the 
    middle element of the array. If the array is sorted, this comparison tells us with absolute 
    certainty whether the target lies in the left half (if target is smaller than middle) or 
    the right half (if target is larger than middle). 
    
    If the array was unsorted, no such assumption could be made: the target could be on either side 
    of the middle element regardless of whether it is smaller or larger. Thus, we would not be 
    able to discard half of the array at each step, and binary search would fail.
    """
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1

def main():
    # Unsorted test list with 11 elements (at least 10 elements)
    unsorted_list = [42, 7, 19, 99, 12, 54, 33, 8, 90, 21, 65]
    print(f"Sample Unsorted List (Length {len(unsorted_list)}): {unsorted_list}")
    
    # Testing targets
    targets_to_test = [33, 100]  # 33 is present, 100 is absent
    
    print("\n--- Testing Linear Search (on Unsorted List) ---")
    for target in targets_to_test:
        idx = linear_search(unsorted_list, target)
        if idx != -1:
            print(f"Target '{target}' found at index {idx}.")
        else:
            print(f"Target '{target}' was not found in the list (returned {idx}).")
            
    # Binary search requires the array to be sorted
    sorted_list = sorted(unsorted_list)
    print(f"\nSample Sorted List (for Binary Search): {sorted_list}")
    
    print("\n--- Testing Binary Search (on Sorted List) ---")
    for target in targets_to_test:
        idx = binary_search(sorted_list, target)
        if idx != -1:
            print(f"Target '{target}' found at index {idx} in the sorted list.")
        else:
            print(f"Target '{target}' was not found in the sorted list (returned {idx}).")

if __name__ == "__main__":
    main()
