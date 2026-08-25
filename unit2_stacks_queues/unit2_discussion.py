"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        self.items = []

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.
        # New values are added to the end, making the most recent item come out first.
        self.items.append(value)

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?
        if self.is_empty():
            return "Stack is empty. Nothing to pop."
        return self.items.pop()

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.
        # Peek shows the most recent item without changing the stack.
        if self.is_empty():
            return "Stack is empty. Nothing to peek."
        return self.items[-1]

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        return len(self.items) == 0


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        self.items = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.
        # New values are added to the back, so older values leave first.
        self.items.append(value)

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.
        if self.is_empty():
            return "Queue is empty. Nothing to dequeue."
        return self.items.popleft()

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.
        # Front shows the oldest item without removing it from the queue.
        if self.is_empty():
            return "Queue is empty. Nothing at the front."
        return self.items[0]

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        return len(self.items) == 0


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.

    print("\n=== STACK DEMO ===")

    browser_history = Stack()

    print("Adding pages to browser history:")
    browser_history.push("Home Page")
    browser_history.push("Products Page")
    browser_history.push("Shopping Cart")
    browser_history.push("Checkout Page")

    print("Top page:", browser_history.peek())

    print("\nDemonstrating LIFO behavior:")
    print("Going back from:", browser_history.pop())
    print("Going back from:", browser_history.pop())
    print("Going back from:", browser_history.pop())
    print("Going back from:", browser_history.pop())

    print("\nTrying to pop from an empty stack:")
    print(browser_history.pop())

    print("\nTrying to peek at an empty stack:")
    print(browser_history.peek())

    print("\nTesting a single-item stack:")
    one_item_stack = Stack()
    one_item_stack.push("Only Item")
    print("Removed:", one_item_stack.pop())
    print("Is the stack empty?", one_item_stack.is_empty())

    # ===============================
    # TODO (Student): QUEUE DEMO
    # ===============================
    # Requirements:
    # 1. Create a Queue object.
    # 2. Add at least 4 values to the queue.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate FIFO behavior.
    # 5. Show what happens when dequeue() is used on an empty queue.
    #
    # Edge Cases:
    # 6. Show what happens when front() is used on an empty queue.
    # 7. Create a queue with only one item, remove it,
    #    and verify the queue is empty afterward.

    print("\n=== QUEUE DEMO ===")

    coffee_line = Queue()

    print("Customers joining the coffee shop line:")
    coffee_line.enqueue("Customer 1")
    coffee_line.enqueue("Customer 2")
    coffee_line.enqueue("Customer 3")
    coffee_line.enqueue("Customer 4")

    print("First customer in line:", coffee_line.front())

    print("\nDemonstrating FIFO behavior:")
    print("Serving:", coffee_line.dequeue())
    print("Serving:", coffee_line.dequeue())
    print("Serving:", coffee_line.dequeue())
    print("Serving:", coffee_line.dequeue())

    print("\nTrying to dequeue from an empty queue:")
    print(coffee_line.dequeue())

    print("\nTrying to view the front of an empty queue:")
    print(coffee_line.front())

    print("\nTesting a single-item queue:")
    one_item_queue = Queue()
    one_item_queue.enqueue("Only Customer")
    print("Removed:", one_item_queue.dequeue())
    print("Is the queue empty?", one_item_queue.is_empty())


if __name__ == "__main__":
    main()
