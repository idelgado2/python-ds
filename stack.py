class Stack:
    def __init__(self):
        # Initialize an empty list to store stack items
        self.items = []

    def push(self, item):
        # Add an item to the top of the stack
        self.items.append(item)

    def pop(self):
        # Remove and return the top item of the stack
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self):
        # Return the top item without removing it
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]

    def is_empty(self):
        # Check if the stack is empty
        return len(self.items) == 0

    def size(self):
        # Return the number of items in the stack
        return len(self.items)

    def __repr__(self):
        # Return a string representation of the stack
        return f"Stack({self.items})"

# Example usage
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack)         # Output: Stack([1, 2, 3])
print(stack.pop())   # Output: 3
print(stack.peek())  # Output: 2
print(stack.size())  # Output: 2
print(stack.is_empty())  # Output: False
