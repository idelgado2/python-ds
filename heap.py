class MinHeap:
    def __init__(self):
        # Initialize an empty list to store heap elements
        self.heap = []

    def _parent(self, index):
        # Return the index of the parent node
        return (index - 1) // 2

    def _left_child(self, index):
        # Return the index of the left child
        return 2 * index + 1

    def _right_child(self, index):
        # Return the index of the right child
        return 2 * index + 2

    def insert(self, value):
        # Add a new value to the heap and maintain heap property
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        # Move the value at index up to its correct position
        parent = self._parent(index)
        while index > 0 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = self._parent(index)

    def extract_min(self):
        # Remove and return the smallest value (root) from the heap
        if not self.heap:
            raise IndexError("extract from empty heap")
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def _heapify_down(self, index):
        # Move the value at index down to its correct position
        smallest = index
        left = self._left_child(index)
        right = self._right_child(index)

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

    def __repr__(self):
        # Return a string representation of the heap
        return f"MinHeap({self.heap})"

# Example usage
h = MinHeap()
h.insert(5)
h.insert(3)
h.insert(8)
h.insert(1)
print(h)                # Output: MinHeap([1, 3, 8, 5])
print(h.extract_min())  # Output: 1
print(h)                # Output: MinHeap([3, 5, 8])
h.insert(2)
print(h)                # Output: MinHeap([2, 3, 8, 5])
