"""
Exercise 4 (Set Comprehension):
Given a list of numbers [1, 2, 2, 3, 4, 4, 5, 5, 5], use a set comprehension to create a set of their cubes.
"""

list_of_numbers = [1, 2, 2, 3, 4, 4, 5, 5, 5]

cubes = {n**3 for n in list_of_numbers}
print(cubes)