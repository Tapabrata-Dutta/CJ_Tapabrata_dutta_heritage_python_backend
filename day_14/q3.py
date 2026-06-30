class Node:
    """Represents a single node in the linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None


    def __repr__(self):
        return f'Node({self.data})'




class LinkedList:
    """
    A complete Singly Linked List implementation.
    Supports insert, delete, search, traverse, reverse.
    """
def __init__(self):
        self.head = None
        self._size = 0        # Track size for O(1) length()


    # ─── INSERT OPERATIONS ────────────────────────────


def insert_at_beginning(self, data):
        """Insert node at the start. Time: O(1)"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self._size += 1


def insert_at_end(self, data):
        """Insert node at the end. Time: O(n)"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self._size += 1


def insert_at_position(self, data, position):
        """Insert at index. Time: O(n)"""
        if position < 0 or position > self._size:
            raise IndexError(f'Position {position} out of range')
        if position == 0:
            return self.insert_at_beginning(data)
        new_node = Node(data)
        current = self.head
        for _ in range(position - 1):
            current = current.next
        new_node.next = current.next
        current.next = new_node
        self._size += 1


    # ─── DELETE OPERATIONS ────────────────────────────


def delete_by_value(self, value):
        """Delete first node with given value. Time: O(n)"""
        if self.head is None:
            raise ValueError('Cannot delete from empty list')
        if self.head.data == value:
            self.head = self.head.next
            self._size -= 1
            return
        current = self.head
        while current.next is not None:
            if current.next.data == value:
                current.next = current.next.next
                self._size -= 1
                return
            current = current.next
        raise ValueError(f'{value} not found in list')


def delete_at_position(self, position):
        """Delete node at given index. Time: O(n)"""
        if position < 0 or position >= self._size:
             raise IndexError(f'Position {position} out of range')
        if position == 0:
            self.head = self.head.next
            self._size -= 1
            return
        current = self.head
        for _ in range(position - 1):
            current = current.next
        current.next = current.next.next
        self._size -= 1


    # ─── SEARCH ───────────────────────────────────────


def search(self, value):
        """Return index of value, or -1 if not found. Time: O(n)"""
        current = self.head
        index = 0
        while current is not None:
            if current.data == value:
                return index
            current = current.next
            index += 1
        return -1


    # ─── UTILITY ──────────────────────────────────────


def length(self):
        """Return number of nodes. Time: O(1)"""
        return self._size


def is_empty(self):
        return self.head is None


def traverse(self):
        """Print all elements. Time: O(n)"""
        elements = []
        current = self.head
        while current is not None:
            elements.append(str(current.data))
            current = current.next
        print(' → '.join(elements) + ' → None')


def __str__(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return ' → '.join(elements) + ' → None'


def __len__(self):
        return self._size

