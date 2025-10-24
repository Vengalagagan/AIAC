class Queue:
    """A simple queue implementation using a Python list."""

    def __init__(self):
        """Initializes an empty queue."""
        self._items = []

    def enqueue(self, item):
        """Adds an item to the end of the queue.

        Args:
            item: The item to add to the queue.
        """
        self._items.append(item)

    def dequeue(self):
        """Removes and returns the item at the front of the queue.

        Returns:
            The item at the front of the queue.

        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Cannot dequeue from empty queue")
        return self._items.pop(0)

    def is_empty(self):
        """Checks if the queue is empty.

        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return len(self._items) == 0


# Test the Queue
if __name__ == "__main__":
    print("Testing Queue:")
    queue = Queue()
    
    # Test enqueue
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(f"After enqueuing 1, 2, 3: {queue._items}")
    
    # Test dequeue
    print(f"Dequeue: {queue.dequeue()}")
    print(f"After dequeue: {queue._items}")
    
    print(f"Is empty: {queue.is_empty()}")
    
    # Test more operations
    queue.enqueue(4)
    queue.enqueue(5)
    print(f"After enqueuing 4, 5: {queue._items}")
    print(f"Dequeue: {queue.dequeue()}")
    print(f"Final queue: {queue._items}")