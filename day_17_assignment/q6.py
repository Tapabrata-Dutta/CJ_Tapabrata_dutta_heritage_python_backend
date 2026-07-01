# Q6: Implement Quick Sort using the last element as pivot

def quick_sort_last_pivot(arr, low=0, high=None):
    """
    Quick Sort with last element as pivot.
    
    Args:
        arr: List to be sorted
        low: Starting index
        high: Ending index
    
    Returns:
        Sorted array
    """
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        # Partition and get pivot index
        pivot_index = partition(arr, low, high)
        # Sort left and right parts
        quick_sort_last_pivot(arr, low, pivot_index - 1)
        quick_sort_last_pivot(arr, pivot_index + 1, high)
    
    return arr

def partition(arr, low, high):
    """
    Partition array with last element as pivot.
    """
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# Example usage
if __name__ == "__main__":
    numbers = [64, 34, 25, 12, 22, 11, 90, 88, 45, 50]
    
    print("Original array:")
    print(numbers)
    
    sorted_array = quick_sort_last_pivot(numbers.copy())
    
    print("\nSorted array:")
    print(sorted_array)
    
    # Another example
    scores = [85, 92, 78, 95, 88, 76, 90, 82]
    print("\nScores before sorting:")
    print(scores)
    
    sorted_scores = quick_sort_last_pivot(scores.copy())
    print("\nScores after sorting:")
    print(sorted_scores)
