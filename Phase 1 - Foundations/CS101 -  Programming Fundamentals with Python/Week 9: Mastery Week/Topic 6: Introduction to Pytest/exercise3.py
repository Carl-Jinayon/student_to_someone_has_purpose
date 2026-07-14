"""
Exercise 3 (Testing a Class):
Define a simple Counter class with:

- __init__() initializes self.count = 0
- increment() adds 1 to the count
- decrement() subtracts 1 from the count
- reset() sets the count to 0
- get_count() returns the current count

Write tests to verify each method works correctly.
"""

class Counter:
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1
    
    def reset(self):
        self.count = 0
    
    def get_count(self):
        return self.count