"""
Exercise 2 (map):
Given a list of temperatures in Celsius [0, 20, 30, 40], use map and a lambda
to convert them to Fahrenheit (F = C * 9/5 + 32). Print the result as a list.
"""

my_list = [0, 20, 30, 40]

print(list(map(lambda cel: cel * 9/5 + 32, my_list)))