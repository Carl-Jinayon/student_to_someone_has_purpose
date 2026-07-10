#!/usr/bin/env python3
"""
================================================================================
HANDOUT #6: FUNCTIONS (Step 6)
================================================================================
Student: ________________________________
Date: ___________________________________

This handout covers:
    1. Defining and calling functions
    2. Parameters and arguments
    3. The return statement
    4. Default parameters
    5. Local vs global scope (basic)
    6. Recursion (basic)

Prerequisites used: int, str, bool, print(), input(), operators, control flow.
No lists, no dictionaries.
================================================================================
"""

print("\n" + "="*70)
print("STEP 6: FUNCTIONS")
print("="*70)

# =============================================================================
# PART 1: Basic Function Definition and Call
# =============================================================================

print("\n" + "-"*50)
print("PART 1: Basic Function")
print("-"*50)

def greet():
    """A simple function that prints a greeting."""
    print("Hello, world!")

greet()   # Call the function
greet()   # Call it again


# =============================================================================
# PART 2: Parameters and Arguments
# =============================================================================

print("\n" + "-"*50)
print("PART 2: Parameters and Arguments")
print("-"*50)

def greet_person(name):
    """Print a personalized greeting."""
    print(f"Hello, {name}!")

greet_person("Alice")
greet_person("Bob")

def add(a, b):
    """Print the sum of two numbers."""
    print(f"{a} + {b} = {a + b}")

add(5, 3)
add(10, 20)


# =============================================================================
# PART 3: return Statement
# =============================================================================

print("\n" + "-"*50)
print("PART 3: return")
print("-"*50)

def multiply(a, b):
    """Return the product of two numbers."""
    return a * b

# Store the result
product = multiply(4, 5)
print(f"Product: {product}")

# Use the result directly
print(f"2 * 3 = {multiply(2, 3)}")

# Return stops the function early
def check_age(age):
    if age < 0:
        return "Invalid age"   # This returns immediately
    if age >= 18:
        return "Adult"
    return "Minor"

print(check_age(25))   # Adult
print(check_age(-5))   # Invalid age


# =============================================================================
# PART 4: Default Parameters
# =============================================================================

print("\n" + "-"*50)
print("PART 4: Default Parameters")
print("-"*50)

def greet_with_title(name, title="Mr."):
    """Greet a person with an optional title."""
    print(f"Hello, {title} {name}!")

greet_with_title("Smith")        # Uses default: Mr.
greet_with_title("Smith", "Dr.") # Overrides default


# =============================================================================
# PART 5: Scope (Local vs Global)
# =============================================================================

print("\n" + "-"*50)
print("PART 5: Scope")
print("-"*50)

global_var = "I am global"

def show_scope():
    local_var = "I am local"
    print("Inside function:")
    print(f"  {global_var}")   # Can read global
    print(f"  {local_var}")    # Can read local

show_scope()
# print(local_var)  # ERROR: local_var does not exist outside the function

# If you try to assign to a global variable inside a function, it creates a new
# local variable unless you use the 'global' keyword.
x = 10
def modify_x():
    x = 20   # This creates a local x, it does NOT change the global x
    print(f"Inside modify_x: x = {x}")

modify_x()
print(f"Outside: x = {x}")  # Still 10


# =============================================================================
# PART 6: Recursion (Function Calling Itself)
# =============================================================================

print("\n" + "-"*50)
print("PART 6: Recursion")
print("-"*50)

def factorial(n):
    """Return n! (n * (n-1) * ... * 1)."""
    if n == 1:          # Base case
        return 1
    else:               # Recursive case
        return n * factorial(n - 1)

print(f"factorial(5) = {factorial(5)}")  # 120

# Step-by-step: factorial(5) -> 5 * factorial(4) -> 4 * factorial(3) -> ...
#                                     -> 3 * factorial(2) -> 2 * factorial(1) -> 1

# WARNING: Without a base case, recursion goes infinite.
# def bad_recursion(n):
#     return bad_recursion(n)   # RecursionError


# =============================================================================
# COMMON MISTAKES
# =============================================================================

print("\n" + "-"*50)
print("COMMON MISTAKES TO AVOID")
print("-"*50)

print("\n❌ Mistake 1: Forgetting the colon")
print("   # def hello()  # SyntaxError: missing ':'")
print("   #     print('Hi')")

print("\n❌ Mistake 2: Indentation errors")
print("   # def hello():")
print("   # print('Hi')  # IndentationError")

print("\n❌ Mistake 3: Forgetting to return")
print("   # def add(a, b):")
print("   #     result = a + b")
print("   # # No return -> returns None")
print("   # x = add(2, 3)  # x is None")

print("\n❌ Mistake 4: Code after return")
print("   # def test():")
print("   #     return 5")
print("   #     print('This never runs')  # Unreachable")

print("\n❌ Mistake 5: Infinite recursion")
print("   # def crash():")
print("   #     return crash()  # RecursionError")


# =============================================================================
# CORE EXERCISES
# =============================================================================

print("\n" + "="*70)
print("CORE EXERCISES (Step 6 Mastery Check)")
print("="*70)

print("""
EXERCISE 1 (Basic):
Write a function square(x) that returns the square of a number.
Call it with 5 and print the result.

EXERCISE 2 (Multiple Parameters):
Write a function calculate_rectangle_area(length, width) that returns the area.
Calculate the area of a rectangle with length 10 and width 5, and print it.

EXERCISE 3 (Default Parameters):
Write a function greet_user(name, greeting="Hello") that prints:
    "Hello, name!" if no greeting is provided
    "greeting, name!" if a custom greeting is provided
Test it with greet_user("Alice") and greet_user("Bob", "Hi").

EXERCISE 4 (Return and Logic):
Write a function is_even(num) that returns True if the number is even,
and False if it is odd. (Hint: use the modulo operator %.)

EXERCISE 5 (Recursion):
Write a recursive function sum_to_n(n) that returns the sum of all
numbers from 1 to n. (Hint: sum_to_n(5) should return 15.)
""")


# =============================================================================
# 📌 ADVANCED EXTENSION (Optional - For Wandering)
# =============================================================================

print("\n" + "="*70)
print("ADVANCED EXTENSION (Optional - For Wandering)")
print("="*70)

print("""
The following concepts are EXTRA. They are NOT required for Step 6 mastery.
Read them if you are curious.
""")

# 1. *args (variable positional arguments)
print("\n--- 1. *args (Variable Positional Arguments) ---")
def print_all_args(*args):
    print(f"Arguments: {args}")   # args is a tuple

print_all_args(1, 2, 3, "hello", True)

# 2. **kwargs (variable keyword arguments)
print("\n--- 2. **kwargs (Variable Keyword Arguments) ---")
def print_all_kwargs(**kwargs):
    print(f"Keyword arguments: {kwargs}")   # kwargs is a dict

print_all_kwargs(name="Alice", age=30, city="Manila")

# 3. lambda (anonymous function)
print("\n--- 3. lambda (Anonymous Function) ---")
square_lambda = lambda x: x * x
print(f"lambda square of 5: {square_lambda(5)}")

# 4. Docstrings
print("\n--- 4. Docstrings ---")
def documented_function():
    """This function demonstrates a docstring."""
    pass

print(f"Docstring: {documented_function.__doc__}")

# 5. Functions as objects
print("\n--- 5. Functions as First-Class Citizens ---")
def hello():
    return "Hello"

say_hello = hello   # Assign function to variable
print(say_hello())  # Call through the variable

print("\n" + "="*70)
print("END OF HANDOUT #6")
print("="*70)