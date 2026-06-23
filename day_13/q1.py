class Stack:
    """A LIFO Stack implemented using Python list."""
 
    def __init__(self):
        self._data = []        # Internal list — end = TOP
 
    def push(self, item):
        """Add item to the TOP of the stack.  Time: O(1)"""
        self._data.append(item)     # append() → adds to END (top)
 
    def pop(self):
        """Remove & return TOP item.  Time: O(1)"""
        if self.is_empty():
            raise IndexError("pop from an empty stack")
        return self._data.pop()     # pop() → removes from END (top)
 
    def peek(self):
        """Return TOP item WITHOUT removing.  Time: O(1)"""
        if self.is_empty():
            raise IndexError("peek from an empty stack")
        return self._data[-1]       # Index -1 = last element = top
 
    def is_empty(self):
        """Return True if no elements in stack.  Time: O(1)"""
        return len(self._data) == 0
 
    def size(self):
        """Return count of elements.  Time: O(1)"""
        return len(self._data)
 
    def __repr__(self):
        if self.is_empty():
            return "Stack: [EMPTY]"
        return f"Stack [bottom→top]: {self._data}"
    
def reverse_string(s):
    """Reverse a string using a stack."""
    stack = Stack()
 
    # Push every character onto the stack
    for char in s:
        stack.push(char)
 
    # Pop all characters — LIFO gives reverse order
    result = ''
    while not stack.is_empty():
        result += stack.pop()
 
    return result
 
 
print(reverse_string("Hello"))        # olleH
print(reverse_string("Python"))       # nohtyP
print(reverse_string("racecar"))      # racecar (palindrome!)
print(reverse_string("Stack"))

def is_balanced(expr):
    stack = Stack()   # Reuse our Stack class
    opening = set('({[')
    match   = {')':'(', '}':'{', ']':'['}
 
    for ch in expr:
        if ch in opening:
            stack.push(ch)           # Push every opening bracket
        elif ch in match:             # It's a closing bracket
            if stack.is_empty():
                return False          # Nothing to match against
            top = stack.pop()
            if top != match[ch]:
                return False          # Wrong pair e.g. ( closed by ]
 
    return stack.is_empty()           # Extra opens → not balanced
 
 
# ---- Comprehensive Test Cases ----
test_cases = [
    ("({[]})",    True,  "Correctly nested"),
    ("()[]{}", True,  "Sequential — all correct"),
    ("([)]",     False, "Wrong close order"),
    ("((((",     False, "Only opens, no close"),
    ("}}}}",     False, "Only closes, no open"),
    ("{[()]}",   True,  "Triple nested"),
    ("",         True,  "Empty string"),
    ("a+(b*c)",  True,  "Embedded in expression"),
    ("{[(])}",   False, "Interleaved wrong order"),
]
 
print(f'{'Expression':<16} {'Expected':<10} {'Got':<10} {'Status'}')
print('-' * 55)
for expr, expected, desc in test_cases:
    result = is_balanced(expr)
    status = 'PASS' if result == expected else 'FAIL'
    print(f'{expr!r:<16} {str(expected):<10} {str(result):<10} [{status}] {desc}')

