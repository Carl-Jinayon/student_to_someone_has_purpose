"""
Exercise 1 (Basic Function):
Write a function square(x) that returns the square of a number. 
Then call it with 5 and print the result.
"""

def square(x):
    return x * x

print(square(5))

"""
Exercise 2 (Multiple Parameters):
Write a function calculate_rectangle_area(length, width) that returns the area. 
Then calculate the area of a rectangle with length 10 and width 5, and print it.
"""

def calculate_rectangle_area(length, width):
    return length * width

print(calculate_rectangle_area(10, 5))

"""
Exercise 3 (Default Parameters):
Write a function greet_user(name, greeting="Hello") 
that prints "Hello, name!" if no greeting is provided, 
otherwise prints "greeting, name!".
Test it with greet_user("Alice") and greet_user("Bob", "Hi").
"""

def greet_user(name, greeting="Hello"):
    print(f"{greeting}, {name}!")
    return

greet_user("Alice")
greet_user("Bob", "Hi")

"""
Exercise 4 (Return and Logic):
Write a function is_even(num) that 
returns True if the number is even, and False if it is odd. 
(Hint: use the modulo operator %.)
"""

def is_even(num):
    return True if num % 2 == 0 else False

print(is_even(2))

"""
Exercise 5 (Recursion):
Write a recursive function sum_to_n(n)
that returns the sum of all numbers from 1 to n. 
(Hint: sum_to_n(5) should return 15.)
"""

def sum_to_n(n):
    if n == 1:
        return n
    else:
        return n + sum_to_n(n - 1)

print(sum_to_n(15))

print(sum("fdsfsda"))