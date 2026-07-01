# Q4: Implement Merge Sort for transaction amounts

def merge_sort(transactions):
    """
    Sort transaction amounts using Merge Sort.
    
    Args:
        transactions: List of tuples (transaction_id, amount, date)
    
    Returns:
        Sorted list of transactions by amount
    """
    if len(transactions) <= 1:
        return transactions
    
    # Divide
    mid = len(transactions) // 2
    left = merge_sort(transactions[:mid])
    right = merge_sort(transactions[mid:])
    
    # Merge
    return merge(left, right)

def merge(left, right):
    """Merge two sorted lists"""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i][1] <= right[j][1]:  # Compare by amount (index 1)
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# Example usage
if __name__ == "__main__":
    transactions = [
        ("T001", 5000, "2024-01-15"),
        ("T002", 2500, "2024-01-14"),
        ("T003", 7500, "2024-01-13"),
        ("T004", 1200, "2024-01-12"),
        ("T005", 9000, "2024-01-11"),
        ("T006", 3800, "2024-01-10")
    ]
    
    print("Original transactions:")
    for tid, amount, date in transactions:
        print(f"  ID: {tid}, Amount: ${amount}, Date: {date}")
    
    sorted_transactions = merge_sort(transactions)
    
    print("\nTransactions sorted by amount:")
    for tid, amount, date in sorted_transactions:
        print(f"  ID: {tid}, Amount: ${amount}, Date: {date}")
