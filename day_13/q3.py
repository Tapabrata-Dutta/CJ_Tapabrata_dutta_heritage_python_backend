from collections import deque
 
class Queue:
    """FIFO Queue implemented with collections.deque."""
 
    def __init__(self):
        self._data = deque()     # Doubly-linked list under the hood
 
    def enqueue(self, item):
        """Add item to the REAR.  Time: O(1)"""
        self._data.append(item)      # append() → adds to RIGHT (rear)
 
    def dequeue(self):
        """Remove and return FRONT item.  Time: O(1)"""
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._data.popleft()  # popleft() → removes from LEFT (front)
 
    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self._data[0]         # Index 0 = front element
 
    def is_empty(self):
        return len(self._data) == 0
 
    def size(self):
        return len(self._data)
 
    def __repr__(self):
        return f"Queue [front→rear]: {list(self._data)}"
