"""
q5_bst.py
This script designs and implements a Binary Search Tree (BST) in Python using OOP.
It supports insert, search, delete (handling leaf, one child, two children cases),
and in-order, pre-order, and post-order traversals.
"""

class Node:
    """A Node in a Binary Search Tree."""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    """A Binary Search Tree implementation."""
    def __init__(self):
        self.root = None

    def insert(self, value):
        """Insert a new value into the BST maintaining the BST property."""
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert_recursive(current_node.left, value)
        else:
            # Handles duplicate values by placing them in the right subtree
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert_recursive(current_node.right, value)

    def search(self, value):
        """Return True if the value exists in the tree, otherwise False."""
        return self._search_recursive(self.root, value)

    def _search_recursive(self, current_node, value):
        if current_node is None:
            return False
        if current_node.value == value:
            return True
        elif value < current_node.value:
            return self._search_recursive(current_node.left, value)
        else:
            return self._search_recursive(current_node.right, value)

    def delete(self, value):
        """Delete a node from the BST, handling leaf, 1-child, and 2-child cases."""
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, current_node, value):
        # Base Case: Value not found
        if current_node is None:
            return None

        # Navigate the tree to find the node to delete
        if value < current_node.value:
            current_node.left = self._delete_recursive(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self._delete_recursive(current_node.right, value)
        else:
            # Node to delete found!
            
            # Case 1 & 2: Leaf node or Node with only one child
            if current_node.left is None:
                return current_node.right
            elif current_node.right is None:
                return current_node.left

            # Case 3: Node with two children
            # Find the in-order successor (smallest value in the right subtree)
            successor = self._find_min(current_node.right)
            # Copy the successor's value to this node
            current_node.value = successor.value
            # Recursively delete the successor node from the right subtree
            current_node.right = self._delete_recursive(current_node.right, successor.value)

        return current_node

    def _find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder(self):
        """In-order traversal: Left -> Root -> Right."""
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)

    def preorder(self):
        """Pre-order traversal: Root -> Left -> Right."""
        result = []
        self._preorder_recursive(self.root, result)
        return result

    def _preorder_recursive(self, node, result):
        if node:
            result.append(node.value)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)

    def postorder(self):
        """Post-order traversal: Left -> Right -> Root."""
        result = []
        self._postorder_recursive(self.root, result)
        return result

    def _postorder_recursive(self, node, result):
        if node:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.value)


def print_traversals(tree, step_name):
    """Utility to print all three tree traversals."""
    print(f"\n--- Traversals {step_name} ---")
    print(f"  In-order:   {tree.inorder()}")
    print(f"  Pre-order:  {tree.preorder()}")
    print(f"  Post-order: {tree.postorder()}")


def main():
    print("==========================================================")
    print("                 Binary Search Tree (BST)                 ")
    print("==========================================================")

    bst = BST()

    # 1. Build a tree with 8 values (at least 8 values)
    # The structure looks like this:
    #             50
    #           /    \
    #         30      70
    #        /  \    /  \
    #       20  40  60  80
    #          /
    #         35
    values = [50, 30, 70, 20, 40, 60, 80, 35]
    print(f"Building BST by inserting: {values}")
    for val in values:
        bst.insert(val)

    # Print all three traversals before delete operations
    print_traversals(bst, "BEFORE Deletion")

    # 2. Demonstrate search operations
    print("\n--- Search Demonstration ---")
    search_tests = [40, 99, 50, 15]
    for val in search_tests:
        print(f"  Search for {val}: {'Found' if bst.search(val) else 'Not Found'}")

    # 3. Demonstrate delete operations (covering all three cases):
    
    # Case 2: One child deletion (40 has left child 35 and no right child)
    print("\n--- Deletion Case 2: Delete Node with One Child (40) ---")
    bst.delete(40)
    print_traversals(bst, "AFTER Deleting 40")

    # Case 1: Leaf node deletion (35 has no children now)
    print("\n--- Deletion Case 1: Delete Leaf Node (35) ---")
    bst.delete(35)
    print_traversals(bst, "AFTER Deleting 35")
    
    # Case 3: Two children deletion (Root node 50 has left child 20 and right child 70)
    print("\n--- Deletion Case 3: Delete Node with Two Children (Root: 50) ---")
    bst.delete(50)
    print_traversals(bst, "AFTER Deleting Root 50")

if __name__ == "__main__":
    main()


"""
tapabratadutta@TAPABRATAs-MacBook-Air Intern_program % python3 /Users/tapabratadutta/Intern_program/final_revolution/q5_bst.py
==========================================================
                 Binary Search Tree (BST)                 
==========================================================
Building BST by inserting: [50, 30, 70, 20, 40, 60, 80, 35]

--- Traversals BEFORE Deletion ---
  In-order:   [20, 30, 35, 40, 50, 60, 70, 80]
  Pre-order:  [50, 30, 20, 40, 35, 70, 60, 80]
  Post-order: [20, 35, 40, 30, 60, 80, 70, 50]

--- Search Demonstration ---
  Search for 40: Found
  Search for 99: Not Found
  Search for 50: Found
  Search for 15: Not Found

--- Deletion Case 2: Delete Node with One Child (40) ---

--- Traversals AFTER Deleting 40 ---
  In-order:   [20, 30, 35, 50, 60, 70, 80]
  Pre-order:  [50, 30, 20, 35, 70, 60, 80]
  Post-order: [20, 35, 30, 60, 80, 70, 50]

--- Deletion Case 1: Delete Leaf Node (35) ---

--- Traversals AFTER Deleting 35 ---
  In-order:   [20, 30, 50, 60, 70, 80]
  Pre-order:  [50, 30, 20, 70, 60, 80]
  Post-order: [20, 30, 60, 80, 70, 50]

--- Deletion Case 3: Delete Node with Two Children (Root: 50) ---

--- Traversals AFTER Deleting Root 50 ---
  In-order:   [20, 30, 60, 70, 80]
  Pre-order:  [60, 30, 20, 70, 80]
  Post-order: [20, 30, 80, 70, 60]
tapabratadutta@TAPABRATAs-MacBook-Air Intern_program % 
"""