"""
Exercise 1 (List Comprehension):
Given a list of numbers [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], use a list comprehension to create a new list containing only the odd numbers squared.
"""
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

my_new_list = [n**2 for n in my_list if n % 2 == 1]
print(my_new_list)

