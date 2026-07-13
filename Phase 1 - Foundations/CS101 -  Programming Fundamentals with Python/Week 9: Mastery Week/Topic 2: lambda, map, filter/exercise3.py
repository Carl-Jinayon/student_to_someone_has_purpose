"""
Exercise 3 (filter):
Given a list of numbers [12, 15, 18, 21, 24, 27], 
use filter and a lambda to keep only numbers divisible by 3 AND greater than 20. Print the result as a list.
"""

my_list = [12, 15, 18, 21, 24, 27]

print(list(filter(lambda x: x % 3 == 0 and x > 20, my_list)))