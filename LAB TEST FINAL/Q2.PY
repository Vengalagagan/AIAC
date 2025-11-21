"""
Stack implementation for parcel tracking history.
Maintains the latest 10 operations only.
"""


class TrackingStack:
    """
    A Stack data structure that stores parcel tracking history.
    Automatically maintains only the latest 10 operations.
    """
    
    MAX_SIZE = 10
    
    def __init__(self):
        """Initialize an empty stack for tracking operations."""
        self.items = []
    
    def push(self, operation):
        """
        Add a new tracking operation to the stack.
        If stack exceeds MAX_SIZE, removes the oldest operation.
        
        Args:
            operation (str): The tracking operation to add
        """
        self.items.append(operation)
        # Remove oldest operation if stack exceeds max size
        if len(self.items) > self.MAX_SIZE:
            self.items.pop(0)
    
    def pop(self):
        """
        Remove and return the most recent tracking operation.
        
        Returns:
            str: The most recent operation, or None if stack is empty
        """
        if self.is_empty():
            return None
        return self.items.pop()
    
    def peek(self):
        """
        View the most recent operation without removing it.
        
        Returns:
            str: The most recent operation, or None if stack is empty
        """
        if self.is_empty():
            return None
        return self.items[-1]
    
    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.items) == 0
    
    def size(self):
        """Return the current number of operations in the stack."""
        return len(self.items)
    
    def get_all(self):
        """Return all operations in the stack (oldest to newest)."""
        return self.items.copy()


def display_menu():
    """Display the interactive menu options."""
    print("\n" + "=" * 60)
    print("PARCEL TRACKING STACK - INTERACTIVE MENU")
    print("=" * 60)
    print("1. Add tracking operation (PUSH)")
    print("2. Remove latest operation (POP)")
    print("3. View latest operation (PEEK)")
    print("4. View all operations")
    print("5. Check stack status")
    print("6. Clear all operations")
    print("7. Exit")
    print("=" * 60)


def interactive_tracking():
    """
    Interactive parcel tracking system with user input.
    
    Allows users to:
    - Add tracking operations
    - Remove the most recent operation
    - View stack contents
    - Clear the stack
    """
    stack = TrackingStack()
    
    print("=" * 60)
    print("PARCEL TRACKING SYSTEM")
    print("=" * 60)
    print(f"Stack capacity: {stack.MAX_SIZE} operations")
    print("The system will track only the latest 10 operations.\n")
    
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-7): ").strip()
        
        if choice == '1':
            # Add operation
            print("\n--- Add New Tracking Operation ---")
            operation = input("Enter tracking operation (e.g., 'Parcel picked up'): ").strip()
            
            if operation:
                stack.push(operation)
                print(f"✓ Operation added successfully!")
                print(f"  Current stack size: {stack.size()}/{stack.MAX_SIZE}")
            else:
                print("✗ Error: Operation cannot be empty!")
        
        elif choice == '2':
            # Remove operation
            print("\n--- Remove Latest Operation ---")
            if stack.is_empty():
                print("✗ Stack is empty! Nothing to remove.")
            else:
                popped = stack.pop()
                print(f"✓ Operation removed:")
                print(f"  {popped}")
                print(f"  Remaining operations: {stack.size()}")
        
        elif choice == '3':
            # View latest operation
            print("\n--- Latest Operation (PEEK) ---")
            if stack.is_empty():
                print("✗ Stack is empty! No operations to view.")
            else:
                latest = stack.peek()
                print(f"✓ Latest operation:")
                print(f"  {latest}")
        
        elif choice == '4':
            # View all operations
            print("\n--- All Operations in Stack ---")
            if stack.is_empty():
                print("✗ Stack is empty!")
            else:
                all_ops = stack.get_all()
                print(f"Operations (oldest to newest):")
                for i, op in enumerate(all_ops, 1):
                    print(f"  {i}. {op}")
        
        elif choice == '5':
            # Check stack status
            print("\n--- Stack Status ---")
            print(f"Current size: {stack.size()}")
            print(f"Maximum capacity: {stack.MAX_SIZE}")
            print(f"Stack empty: {stack.is_empty()}")
            if not stack.is_empty():
                print(f"Latest operation: {stack.peek()}")
        
        elif choice == '6':
            # Clear stack
            print("\n--- Clear Stack ---")
            confirm = input("Are you sure you want to delete all operations? (yes/no): ").strip().lower()
            if confirm == 'yes':
                stack = TrackingStack()
                print("✓ All operations cleared!")
            else:
                print("✗ Clear operation cancelled.")
        
        elif choice == '7':
            # Exit
            print("\n" + "=" * 60)
            print("Thank you for using Parcel Tracking System!")
            print("=" * 60)
            break
        
        else:
            print("✗ Invalid choice! Please enter a number between 1 and 7.")


# Test cases
if __name__ == "__main__":
    interactive_tracking()