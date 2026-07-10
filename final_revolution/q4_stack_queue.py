"""
q4_stack_queue.py
This script demonstrates Stack and Queue data structures and their applications.
- Part A: Balanced Parentheses Checker using a custom Stack (implemented via list).
- Part B: Ticket Counter Queue Simulation using collections.deque.
"""

from collections import deque

# ==============================================================================
# PART A: Balanced Parentheses Checker
# ==============================================================================

class Stack:
    """
    A custom Stack class implemented using a standard Python list.
    Follows Last-In, First-Out (LIFO) protocol.
    """
    def __init__(self):
        self._items = []

    def push(self, item):
        """Add an item to the top of the stack."""
        self._items.append(item)

    def pop(self):
        """Remove and return the top item from the stack. Raises IndexError if empty."""
        if self.is_empty():
            raise IndexError("Pop error: Stack is empty.")
        return self._items.pop()

    def peek(self):
        """Return the top item of the stack without removing it. Returns None if empty."""
        if self.is_empty():
            return None
        return self._items[-1]

    def is_empty(self):
        """Return True if the stack contains no elements, False otherwise."""
        return len(self._items) == 0

    def size(self):
        """Return the current number of elements in the stack."""
        return len(self._items)


def is_balanced(bracket_str):
    """
    Determines if a string of brackets (containing '(', ')', '{', '}', '[', ']') 
    is balanced and correctly nested.
    """
    stack = Stack()
    # Map closing brackets to their corresponding opening brackets
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in bracket_str:
        # If it's an opening bracket, push to the stack
        if char in mapping.values():
            stack.push(char)
        # If it's a closing bracket
        elif char in mapping:
            # Check if stack is empty (no matching opening bracket) 
            # or if the popped element doesn't match
            if stack.is_empty() or stack.pop() != mapping[char]:
                return False
        # Ignore non-bracket characters if any are present
    
    # If the stack is empty, all opening brackets were matched and closed correctly
    return stack.is_empty()


# ==============================================================================
# PART B: Ticket Counter Queue Simulation
# ==============================================================================

class Queue:
    """
    A custom Queue class implemented using collections.deque.
    Follows First-In, First-Out (FIFO) protocol.
    """
    def __init__(self):
        self._items = deque()

    def enqueue(self, item):
        """Add an item to the back of the queue."""
        self._items.append(item)

    def dequeue(self):
        """Remove and return the front item from the queue. Raises IndexError if empty."""
        if self.is_empty():
            raise IndexError("Dequeue error: Queue is empty.")
        return self._items.popleft()

    def is_empty(self):
        """Return True if the queue is empty, False otherwise."""
        return len(self._items) == 0

    def size(self):
        """Return the current number of elements in the queue."""
        return len(self._items)

    def to_list(self):
        """Return a list representation of the queue for display purposes."""
        return list(self._items)


def main():
    print("==========================================================")
    print("         PART A: Balanced Parentheses Checker             ")
    print("==========================================================")
    
    # Test cases: at least 5 different strings
    test_cases = [
        "()",                 # True (simple match)
        "({[]})",             # True (perfectly nested)
        "()[]{}",             # True (sequential matches)
        "(]",                 # False (mismatched brackets)
        "([)]",               # False (incorrect nesting order)
        "(((({}))))",         # True (nested same brackets)
        "({[}",               # False (unmatched/unclosed brackets)
        "["                   # False (single opening bracket)
    ]
    
    print("Running bracket checker on test strings:")
    for expression in test_cases:
        result = is_balanced(expression)
        print(f"  String: {expression:12} | Balanced? {result}")

    print("\n==========================================================")
    print("             PART B: Ticket Counter Simulation            ")
    print("==========================================================")
    
    ticket_counter = Queue()
    print(f"Initial Queue State: {ticket_counter.to_list()}")
    
    # Customers arriving
    arrivals = ["Alice", "Bob", "Charlie", "David", "Eve"]
    print("\n--- Customers Arriving and Enqueueing ---")
    for customer in arrivals:
        ticket_counter.enqueue(customer)
        print(f"  [Enqueue] {customer:8} joined the line. Current Queue: {ticket_counter.to_list()}")
        
    # Customers being served
    print("\n--- Serving Customers (Dequeueing) ---")
    while not ticket_counter.is_empty():
        served_customer = ticket_counter.dequeue()
        print(f"  [Dequeue] {served_customer:8} was served.  Current Queue: {ticket_counter.to_list()}")
        
    print("\nTicket line simulation complete. Queue is empty.")

if __name__ == "__main__":
    main()


"""
tapabratadutta@TAPABRATAs-MacBook-Air Intern_program % python3 /Users/tapabratadutta/Intern_program/final_revolution/q4_stack_queue.py
==========================================================
         PART A: Balanced Parentheses Checker             
==========================================================
Running bracket checker on test strings:
  String: ()           | Balanced? True
  String: ({[]})       | Balanced? True
  String: ()[]{}       | Balanced? True
  String: (]           | Balanced? False
  String: ([)]         | Balanced? False
  String: (((({}))))   | Balanced? True
  String: ({[}         | Balanced? False
  String: [            | Balanced? False

==========================================================
             PART B: Ticket Counter Simulation            
==========================================================
Initial Queue State: []

--- Customers Arriving and Enqueueing ---
  [Enqueue] Alice    joined the line. Current Queue: ['Alice']
  [Enqueue] Bob      joined the line. Current Queue: ['Alice', 'Bob']
  [Enqueue] Charlie  joined the line. Current Queue: ['Alice', 'Bob', 'Charlie']
  [Enqueue] David    joined the line. Current Queue: ['Alice', 'Bob', 'Charlie', 'David']
  [Enqueue] Eve      joined the line. Current Queue: ['Alice', 'Bob', 'Charlie', 'David', 'Eve']

--- Serving Customers (Dequeueing) ---
  [Dequeue] Alice    was served.  Current Queue: ['Bob', 'Charlie', 'David', 'Eve']
  [Dequeue] Bob      was served.  Current Queue: ['Charlie', 'David', 'Eve']
  [Dequeue] Charlie  was served.  Current Queue: ['David', 'Eve']
  [Dequeue] David    was served.  Current Queue: ['Eve']
  [Dequeue] Eve      was served.  Current Queue: []

Ticket line simulation complete. Queue is empty.
tapabratadutta@TAPABRATAs-MacBook-Air Intern_program % 
"""