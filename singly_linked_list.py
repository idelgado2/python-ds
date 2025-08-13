class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        # Create a new node with the given value
        new_node = Node(value)
        # If the list is empty, set the new node as the head
        if not self.head:
            self.head = new_node
            return
        # Otherwise, traverse to the end of the list
        curr = self.head
        while curr.next:
            curr = curr.next
        # Set the next of the last node to the new node
        curr.next = new_node

    def prepend(self, value):
        # Create a new node and set its next to the current head
        new_node = Node(value)
        new_node.next = self.head
        # Update the head to the new node
        self.head = new_node

    def delete(self, value):
        # Initialize pointers to traverse the list
        curr = self.head
        prev = None
        while curr:
            # If the node to delete is found
            if curr.value == value:
                if prev:
                    # Bypass the current node
                    prev.next = curr.next
                else:
                    # If deleting the head, update head
                    self.head = curr.next
                return True
            prev = curr
            curr = curr.next
        # Value not found
        return False

    def find(self, value):
        # Traverse the list to find the node with the given value
        curr = self.head
        while curr:
            if curr.value == value:
                return curr
            curr = curr.next
        # Value not found
        return None

    def __repr__(self):
        # Collect all node values in a list
        values = []
        curr = self.head
        while curr:
            values.append(str(curr.value))
            curr = curr.next
        # Return a string representation of the list
        return ' -> '.join(values)


sll = SinglyLinkedList()
sll.append(10)
sll.append(20)
sll.prepend(5)
print(sll)  # Output: 5 -> 10 -> 20
sll.delete(10)
print(sll)  # Output: 5 -> 20
node = sll.find(20)
print(node.value if node else "Not found")  # Output: 20