class DynamicArray:
    def __init__(self):
        self.capacity = 1
        self.length = 0
        self.array = self._make_array(self.capacity)

    def _make_array(self, capacity):
        return [None] * capacity

    def _resize(self, new_capacity):
        new_array = self._make_array(new_capacity)
        for i in range(self.length):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, item):
        if self.length == self.capacity:
            self._resize(2 * self.capacity)
        self.array[self.length] = item
        self.length += 1

    def get(self, index):
        if not 0 <= index < self.length:
            raise IndexError('Index out of bounds')
        return self.array[index]

    def set(self, index, value):
        if not 0 <= index < self.length:
            raise IndexError('Index out of bounds')
        self.array[index] = value

    def size(self):
        return self.length

    def __repr__(self):
        return '[' + ', '.join(str(self.array[i]) for i in range(self.length)) + ']'

# Create a new dynamic array
arr = DynamicArray()

# Append elements
arr.append(10)
arr.append(20)
arr.append(30)

# Access elements
print(arr.get(0))  # Output: 10
print(arr.get(1))  # Output: 20

# Set an element
arr.set(1, 99)
print(arr)         # Output: [10, 99, 30]

# Get the size
print(arr.size())  # Output: 3
