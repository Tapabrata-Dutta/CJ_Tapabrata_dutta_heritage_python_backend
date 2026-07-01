# Q10: Validate balanced parentheses in a mathematical expression

class ParenthesesValidator:
    """
    Validates balanced parentheses, brackets, and braces in expressions.
    Uses Stack data structure.
    """
    
    def __init__(self):
        """Initialize validator"""
        self.matching_pairs = {'(': ')', '[': ']', '{': '}'}
    
    def is_balanced(self, expression):
        """
        Check if parentheses are balanced in the expression.
        
        Args:
            expression: String containing mathematical expression
        
        Returns:
            True if balanced, False otherwise
        """
        stack = []
        
        for char in expression:
            if char in self.matching_pairs:  # Opening bracket
                stack.append(char)
            elif char in self.matching_pairs.values():  # Closing bracket
                if not stack:
                    return False
                
                if self.matching_pairs[stack.pop()] != char:
                    return False
        
        return len(stack) == 0
    
    def validate_and_explain(self, expression):
        """
        Validate and provide detailed explanation.
        """
        print(f"\nExpression: {expression}")
        
        if self.is_balanced(expression):
            print("✓ Balanced parentheses")
            return True
        else:
            print("✗ Unbalanced parentheses")
            return False


# Example usage
if __name__ == "__main__":
    validator = ParenthesesValidator()
    
    test_cases = [
        "(2 + 3) * 4",
        "((2 + 3) * (4 - 1))",
        "[1, 2, [3, 4]]",
        "{a + (b * [c])}",
        "(2 + 3) * 4)",  # Extra closing
        "(2 + 3 * 4",     # Missing closing
        "([{1, 2, 3}])",  # Mixed and balanced
        "({[})",          # Mismatched
        "",               # Empty
        "2 + 3 * 4",      # No parentheses
    ]
    
    print("="*50)
    print("Parentheses Validation Test Cases")
    print("="*50)
    
    for expression in test_cases:
        validator.validate_and_explain(expression)
    
    print("\n" + "="*50)
    print("\nTime Complexity: O(n)")
    print("Space Complexity: O(n) for stack")
