from collections import deque

class Queue:
    def __init__(self):
        # Initialize an empty deque to store queue items
        self.queue = deque()

    def enqueue(self, item):
        # Add an item to the end of the queue
        self.queue.append(item)

    def dequeue(self):
        # Remove and return the item from the front of the queue
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.queue.popleft()

    def is_empty(self):
        # Check if the queue is empty
        return len(self.queue) == 0

    def size(self):
        # Return the number of items in the queue
        return len(self.queue)

    def __repr__(self):
        # Return a string representation of the queue
        return f"Queue({list(self.queue)})"

q = Queue()
q.enqueue('a')
q.enqueue('b')
q.enqueue('c')
print(q)            # Output: Queue(['a', 'b', 'c'])
print(q.dequeue())  # Output: a
print(q)            # Output: Queue(['b', 'c'])
print(q.size())     # Output: 2
print(q.is_empty()) # Output: False
