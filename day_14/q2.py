class DNode:
    def __init__(self, data):
        self.data = data
        self.next = None     # Pointer to next node
        self.prev = None     # Pointer to previous node (NEW!)


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

def insert_at_beginning(self, data):
        new_node = DNode(data)
        if self.head is None:          # Empty list
            self.head = new_node
            self.tail = new_node
            return
        # Link new_node ↔ old_head
        new_node.next = self.head      # new → old_head
        self.head.prev = new_node      # old_head ← new (backward link!)
        self.head = new_node           # Update HEAD


def insert_at_end(self, data):
        new_node = DNode(data)
        if self.tail is None:          # Empty list
            self.head = new_node
            self.tail = new_node
            return
        # Link old_tail ↔ new_node
        self.tail.next = new_node      # old_tail → new
        new_node.prev = self.tail      # new ← old_tail (backward link!)
        self.tail = new_node  
def traverse_backward(self):
        current = self.tail            # Start at TAIL
        print('Backward: ', end='')
        while current is not None:
            print(current.data, end=' ↔ ')
            current = current.prev     # Move BACKWARD (use PREV!)
        print('NULL')

def delete_node(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                # Fix PREVIOUS node's next pointer
                if current.prev:                      # Not the HEAD
                    current.prev.next = current.next
                else:                                 # Is the HEAD
                    self.head = current.next
                # Fix NEXT node's prev pointer
                if current.next:                      # Not the TAIL
                    current.next.prev = current.prev
                else:                                 # Is the TAIL
                    self.tail = current.prev
                return  # Node deleted
            current = current.next



