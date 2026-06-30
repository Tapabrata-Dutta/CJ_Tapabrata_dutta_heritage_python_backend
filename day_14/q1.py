class Node:
    def __init__(self, data):
        self.data = data        # Store the value
        self.next = None        # Pointer to next node (default: None)


# Creating nodes
node1 = Node(10)               # Node holds value 10
node2 = Node(20)               # Node holds value 20
node3 = Node(30)
def insert_at_beginning(head, data):
    new_node = Node(data)       # Step 1: Create new node
    new_node.next = head        # Step 2: New node points to old HEAD
    head = new_node             # Step 3: HEAD updated to new node
    return head   

def traverse(head):
    current = head          # Start at the HEAD
    while current is not None:
        print(current.data, end=' → ')  # Visit node
        current = current.next           # Move forward
    print('None')           # End of list

def insert_at_end(head, data):
    new_node = Node(data)
    if head is None:             # Empty list
        return new_node
    current = head
    while current.next is not None:   # Walk to last node
        current = current.next
    current.next = new_node      # Link last node → new node
    return head
def insert_at_position(head, data, position):
    new_node = Node(data)
    if position == 0:            # Insert at beginning
        new_node.next = head
        return new_node
    current = head
    for _ in range(position - 1):   # Walk to node BEFORE position
        if current is None:
            raise IndexError('Position out of range')
        current = current.next
    new_node.next = current.next    # New node → node that was at position
    current.next = new_node         # Previous node → new node
    return head
def search(head, target):
    current = head
    position = 0
    while current is not None:
        if current.data == target:
            return f'Found {target} at position {position}'
        current = current.next
        position += 1
    return f'{target} not found in the list'



