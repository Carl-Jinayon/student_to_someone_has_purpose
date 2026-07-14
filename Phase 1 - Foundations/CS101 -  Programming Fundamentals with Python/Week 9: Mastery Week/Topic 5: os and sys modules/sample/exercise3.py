"""
Exercise 3 (zip to dictionary):
Given two lists:

keys = ["id", "name", "age"]
values = [101, "Alice", 30]

Use zip and dict() to create a dictionary and print it.
"""

keys = ["id", "name", "age"]
values = [101, "Alice", 30]
my_dict = dict()

for key, value in zip(keys, values):
    my_dict[key] = value

print(my_dict)