class Stack:
    """A simple stack implementation using a Python list."""

    def __init__(self):
        """Initializes an empty stack."""
        self._items = []

    def push(self, item):
        """Adds an item to the top of the stack.

        Args:
            item: The item to add to the stack.
        """
        self._items.append(item)

    def pop(self):
        """Removes and returns the item at the top of the stack.

        Returns:
            The item at the top of the stack.

        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("Cannot pop from empty stack")
        return self._items.pop()

    def peek(self):
        """Returns the item at the top of the stack without removing it.

        Returns:
            The item at the top of the stack.

        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("Cannot peek from empty stack")
        return self._items[-1]

    def is_empty(self):
        """Checks if the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return len(self._items) == 0


# Test the Stack
if __name__ == "__main__":
    print("Testing Stack:")
    stack = Stack()
    
    # Test push
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(f"After pushing 1, 2, 3: {stack._items}")
    
    # Test peek
    print(f"Peek (top element): {stack.peek()}")
    
    # Test pop
    print(f"Pop: {stack.pop()}")
    print(f"After pop: {stack._items}")
    
    print(f"Is empty: {stack.is_empty()}")
    
    # Test more operations
    stack.push(4)
    stack.push(5)
    print(f"After pushing 4, 5: {stack._items}")
    print(f"Peek: {stack.peek()}")