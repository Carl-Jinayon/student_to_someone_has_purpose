"""
Exercise 2 (List Comprehension with Strings):
Given a list of words ["apple", "banana", "cherry", "date", "elderberry"], use a list comprehension 
to create a list of words that contain the letter "a", converted to uppercase.
"""

words = ["apple", "banana", "cherry", "date", "elderberry"]

has_a = [word.upper() for word in words if "a" in word]
print(has_a)