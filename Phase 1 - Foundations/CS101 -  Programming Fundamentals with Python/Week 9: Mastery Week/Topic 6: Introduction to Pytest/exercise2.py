"""
Exercise 2 (Testing with Edge Cases):
Write a function calculate_average(numbers) that returns the average of a list of numbers. Then, write tests for:

- [1, 2, 3] → 2.0
- [5, 10] → 7.5
- [] → Should raise ValueError (empty list)
- [0] → 0.0
"""

def calculate_average(numbers: list):
    if not numbers:
        raise ValueError("empty list")
    
    return round(sum(numbers) / len(numbers), 2)