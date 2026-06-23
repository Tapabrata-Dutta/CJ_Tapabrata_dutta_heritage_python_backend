
class Stack:
    """Simple stack implementation."""
    
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)


class TextEditor:
    """Simulates a simple text editor with unlimited undo."""
 
    def __init__(self):
        self.content = ''
        self._undo_stack = Stack()   # Stores (action_name, prev_state)
        self._action_count = 0
 
    def _save_state(self, action_name):
        """Save current state before any action (for undo)."""
        self._undo_stack.push((action_name, self.content))
 
    def type_text(self, text):
        self._save_state(f'type({text!r})')
        self.content += text
        self._log(f'TYPED {text!r}')
 
    def delete_chars(self, n):
        self._save_state(f'delete({n})')
        deleted = self.content[-n:]
        self.content = self.content[:-n]
        self._log(f'DELETED {n} chars ({deleted!r})')
 
    def find_replace(self, old, new_text):
        self._save_state(f'replace({old!r}→{new_text!r})')
        self.content = self.content.replace(old, new_text)
        self._log(f'REPLACED {old!r} with {new_text!r}')
 
    def to_upper(self):
        self._save_state('uppercase')
        self.content = self.content.upper()
        self._log('UPPERCASED')
 
    def undo(self):
        if self._undo_stack.is_empty():
            print('  [UNDO] Nothing left to undo!')
            return
        action, prev = self._undo_stack.pop()
        self.content = prev
        print(f'  [UNDO] Reversed: {action}  →  Content: {self.content!r}')
 
    def _log(self, msg):
        print(f'  {msg:<35}  Content: {self.content!r}')
    def status(self):
        print(f'  Current: {self.content!r}   Undo stack depth: {self._undo_stack.size()}')
 
 
# ---- Simulation ----
ed = TextEditor()
print('=== Editing Session ===')
ed.type_text('Hello')
ed.type_text(', World')
ed.find_replace('World', 'Python')
ed.to_upper()
ed.delete_chars(3)
 
print()
ed.status()
 
print()
print('=== Pressing Ctrl+Z four times ===')
ed.undo()   # Undo delete
ed.undo()   # Undo uppercase
ed.undo()   # Undo replace
ed.undo()   # Undo second type
 
print()
ed.status()
ed.undo()   # Undo first type
ed.undo()   # Nothing left
