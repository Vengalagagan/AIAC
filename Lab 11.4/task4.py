class Node:
    """
    A node in the binary search tree.
    """
    def __init__(self, data):
        """
        Initialize a node with data, and left/right children as None.

        Args:
            data: Value to be stored in the node.
        """
        self.data = data
        self.left = None
        self.right = None

class BST:
    """
    Binary Search Tree implementation with insert, search, and inorder traversal.
    """
    def __init__(self):
        """
        Initializes an empty BST.
        """
        self.root = None

    def insert(self, value):
        """
        Inserts a value into the BST.

        Args:
            value: The value to insert.
        """
        def _insert(node, value):
            if node is None:
                return Node(value)
            if value < node.data:
                node.left = _insert(node.left, value)
            elif value > node.data:
                node.right = _insert(node.right, value)
            # Duplicate values are not inserted in this BST implementation
            return node
        self.root = _insert(self.root, value)

    def search(self, value):
        """
        Searches for a value in the BST.

        Args:
            value: The value to search for.

        Returns:
            bool: True if value is found, False otherwise.
        """
        def _search(node, value):
            if node is None:
                return False
            if value == node.data:
                return True
            elif value < node.data:
                return _search(node.left, value)
            else:
                return _search(node.right, value)
        return _search(self.root, value)

    def inorder_traversal(self):
        """
        Performs in-order traversal of the BST.

        Returns:
            list: List of node values in in-order.
        """
        result = []
        def _inorder(node):
            if node is not None:
                _inorder(node.left)
                result.append(node.data)
                _inorder(node.right)
        _inorder(self.root)
        return result

# Example usage and test
if __name__ == "__main__":
    bst = BST()
    bst.insert(8)
    bst.insert(3)
    bst.insert(10)
    bst.insert(1)
    bst.insert(6)
    bst.insert(14)
    bst.insert(4)
    bst.insert(7)
    bst.insert(13)

    print("Inorder Traversal:", bst.inorder_traversal())
    print("Search 6:", bst.search(6))
    print("Search 15:", bst.search(15))
