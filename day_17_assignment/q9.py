# Q9: Implement a browser Back button using a Stack

class BrowserHistory:
    """
    Browser history manager using a Stack data structure.
    Implements forward and back navigation functionality.
    """
    
    def __init__(self, homepage):
        """Initialize browser with homepage"""
        self.back_stack = []
        self.current_page = homepage
        self.forward_stack = []
    
    def visit(self, url):
        """
        Visit a new URL.
        Pushes current page to back_stack and navigates to new URL.
        """
        self.back_stack.append(self.current_page)
        self.current_page = url
        self.forward_stack.clear()  # Clear forward history when visiting new page
        print(f"Visiting: {url}")
    
    def back(self):
        """
        Go back to previous page.
        Pops from back_stack and pushes current to forward_stack.
        """
        if not self.back_stack:
            print("No back history available")
            return
        
        self.forward_stack.append(self.current_page)
        self.current_page = self.back_stack.pop()
        print(f"Going back to: {self.current_page}")
    
    def forward(self):
        """
        Go forward to next page.
        Pops from forward_stack and pushes current to back_stack.
        """
        if not self.forward_stack:
            print("No forward history available")
            return
        
        self.back_stack.append(self.current_page)
        self.current_page = self.forward_stack.pop()
        print(f"Going forward to: {self.current_page}")
    
    def current(self):
        """Display current page"""
        print(f"Currently on: {self.current_page}")
    
    def show_history(self):
        """Display back and forward history"""
        print(f"Back stack: {self.back_stack}")
        print(f"Current: {self.current_page}")
        print(f"Forward stack: {self.forward_stack}")


# Example usage
if __name__ == "__main__":
    browser = BrowserHistory("google.com")
    
    print("\n--- Browsing History ---\n")
    browser.visit("github.com")
    browser.visit("stackoverflow.com")
    browser.visit("youtube.com")
    browser.visit("linkedin.com")
    
    print("\n--- Current State ---")
    browser.show_history()
    
    print("\n--- Back Navigation ---")
    browser.back()
    browser.back()
    
    print("\n--- Current State ---")
    browser.show_history()
    
    print("\n--- Forward Navigation ---")
    browser.forward()
    
    print("\n--- New Visit (clears forward) ---")
    browser.visit("twitter.com")
    browser.show_history()
