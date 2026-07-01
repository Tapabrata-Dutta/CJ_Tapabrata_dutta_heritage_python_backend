# Q3: Merge two sorted customer lists using the Merge step

def merge_sorted_lists(list1, list2):
    """
    Merge two sorted customer lists.
    
    Args:
        list1: First sorted list of customer records (tuples of customer_id, name, purchase_amount)
        list2: Second sorted list of customer records
    
    Returns:
        Merged sorted list
    """
    merged = []
    i = j = 0
    
    # Compare and merge elements from both lists
    while i < len(list1) and j < len(list2):
        if list1[i][2] <= list2[j][2]:  # Compare by purchase amount
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1
    
    # Add remaining elements
    merged.extend(list1[i:])
    merged.extend(list2[j:])
    
    return merged


# Example usage with customer data
if __name__ == "__main__":
    customers_branch_a = [
        (101, "Alice", 500),
        (103, "Charlie", 1200),
        (105, "Eve", 2000)
    ]
    
    customers_branch_b = [
        (102, "Bob", 800),
        (104, "David", 1500),
        (106, "Frank", 2500)
    ]
    
    print("Branch A customers (sorted by purchase):")
    for cid, name, amount in customers_branch_a:
        print(f"  ID: {cid}, Name: {name}, Amount: ${amount}")
    
    print("\nBranch B customers (sorted by purchase):")
    for cid, name, amount in customers_branch_b:
        print(f"  ID: {cid}, Name: {name}, Amount: ${amount}")
    
    merged = merge_sorted_lists(customers_branch_a, customers_branch_b)
    
    print("\nMerged customer list:")
    for cid, name, amount in merged:
        print(f"  ID: {cid}, Name: {name}, Amount: ${amount}")
