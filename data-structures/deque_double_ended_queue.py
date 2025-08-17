class Deque:
    def __init__(self):
        # Initialize an empty list to store deque items
        self.items = []

    def add_front(self, item):
        # Add an item to the front of the deque (O(n) operation)
        self.items.insert(0, item)

    def add_rear(self, item):
        # Add an item to the rear of the deque (O(1) amortized)
        self.items.append(item)

    def remove_front(self):
        # Remove and return the item from the front of the deque (O(n))
        if self.is_empty():
            raise IndexError("remove from empty deque")
        return self.items.pop(0)

    def remove_rear(self):
        # Remove and return the item from the rear of the deque (O(1))
        if self.is_empty():
            raise IndexError("remove from empty deque")
        return self.items.pop()

    def is_empty(self):
        # Check if the deque is empty
        return len(self.items) == 0

    def size(self):
        # Return the number of items in the deque
        return len(self.items)

    def __repr__(self):
        # Return a string representation of the deque
        return f"Deque({self.items})"

# Example usage

dq = Deque()
dq.add_rear(1)
dq.add_rear(2)
dq.add_front(0)
print(dq)                # Output: Deque([0, 1, 2])
print(dq.remove_front()) # Output: 0
print(dq.remove_rear())  # Output: 2
print(dq)                # Output: Deque([1])
print(dq.size())         # Output: 1
print(dq.is_empty())     # Output: False
