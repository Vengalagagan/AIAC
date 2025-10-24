class Node:
    """A node in a singly linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    """Singly linked list implementation."""

    def __init__(self):
        self.head = None

    def insert_at_end(self, value):
        """Insert a node with the given value at the end of the list."""
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            # Traverse to the last node
            while current.next:
                current = current.next
            current.next = new_node # Link last node's next to new node

    def delete_value(self, value):
        """Delete the first node with the specified value."""
        current = self.head
        prev = None
        while current:
            if current.data == value:
                # If node to delete is head
                if prev is None:
                    # Move head pointer to the next node, removing current
                    self.head = current.next
                else:
                    # Bypass current node by linking previous node's next to current's next
                    prev.next = current.next
                return True  # Value found and deleted
            prev = current
            current = current.next
        return False  # Value not found

    def traverse(self):
        """Traverse the list and return values as a list."""
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next  # Move to next node
        return result

# Example usage and test
if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.insert_at_end(10)
    sll.insert_at_end(20)
    sll.insert_at_end(30)
    print("After inserts:", sll.traverse())

    sll.delete_value(20)
    print("After deleting 20:", sll.traverse())

    sll.delete_value(10)
    print("After deleting 10 (head):", sll.traverse())

    sll.delete_value(30)
    print("After deleting 30 (last element):", sll.traverse())

    # Try deleting a value not in list
    print("Delete 40 (not present):", sll.delete_value(40))
    print("Final list:", sll.traverse())

