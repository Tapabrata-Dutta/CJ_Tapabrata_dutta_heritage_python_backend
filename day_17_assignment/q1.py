# Q1: Sort partially sorted attendance records using Insertion Sort

def insertion_sort_attendance(records):
    """
    Sort partially sorted attendance records by attendance percentage using Insertion Sort.
    
    Args:
        records: List of tuples (name, attendance_percentage)
    
    Returns:
        Sorted list of records
    """
    for i in range(1, len(records)):
        key = records[i]
        j = i - 1
        
        # Compare based on attendance percentage (second element)
        while j >= 0 and records[j][1] > key[1]:
            records[j + 1] = records[j]
            j -= 1
        records[j + 1] = key
    
    return records


# Example usage
if __name__ == "__main__":
    attendance_records = [
        ("Alice", 85),
        ("Bob", 92),
        ("Charlie", 78),
        ("David", 88),
        ("Eve", 95),
        ("Frank", 82)
    ]
    
    print("Original records:")
    print(attendance_records)
    
    sorted_records = insertion_sort_attendance(attendance_records.copy())
    print("\nSorted records (by attendance percentage):")
    for name, attendance in sorted_records:
        print(f"{name}: {attendance}%")
