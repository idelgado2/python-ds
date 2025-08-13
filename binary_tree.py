
# Node class for the binary tree
class TreeNode:
    def __init__(self, value):
        # Store the value of the node
        self.value = value
        # Left child
        self.left = None
        # Right child
        self.right = None


# Binary tree class with insert and traversal methods
class BinaryTree:
    def __init__(self):
        # Initialize the root of the tree
        self.root = None

    def insert(self, value):
        # Insert a value into the binary tree
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        # Helper method to insert recursively
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)

    def inorder(self):
        # Inorder traversal: left, root, right
        def _inorder(node):
            return _inorder(node.left) + [node.value] + _inorder(node.right) if node else []
        return _inorder(self.root)

    def preorder(self):
        # Preorder traversal: root, left, right
        def _preorder(node):
            return [node.value] + _preorder(node.left) + _preorder(node.right) if node else []
        return _preorder(self.root)

    def postorder(self):
        # Postorder traversal: left, right, root
        def _postorder(node):
            return _postorder(node.left) + _postorder(node.right) + [node.value] if node else []
        return _postorder(self.root)

    def __repr__(self):
        # String representation of the tree (inorder)
        return f"BinaryTree({self.inorder()})"

# Example usage
bt = BinaryTree()
bt.insert(5)
bt.insert(3)
bt.insert(7)
bt.insert(1)
bt.insert(4)
print("Inorder:", bt.inorder())    # Output: [1, 3, 4, 5, 7]
print("Preorder:", bt.preorder())  # Output: [5, 3, 1, 4, 7]
print("Postorder:", bt.postorder())# Output: [1, 4, 3, 7, 5]
print(bt)                          # Output: BinaryTree([1, 3, 4, 5, 7])
