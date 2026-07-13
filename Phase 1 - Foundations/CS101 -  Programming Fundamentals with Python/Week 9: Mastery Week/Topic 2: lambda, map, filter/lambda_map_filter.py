#!/usr/bin/env python3
"""
================================================================================
HANDOUT #11: LAMBDA, MAP, AND FILTER (Mastery Week – Topic 2)
================================================================================
Student: ________________________________
Date: ___________________________________

This handout covers:
    1. lambda (anonymous functions)
    2. map() (apply function to iterable)
    3. filter() (filter iterable)
    4. Comparison with comprehensions

Prerequisites used: Functions, Lists, Comprehensions.
================================================================================
"""

print("\n" + "="*70)
print("MASTERY WEEK – TOPIC 2: LAMBDA, MAP, AND FILTER")
print("="*70)

# =============================================================================
# PART 1: lambda (Anonymous Functions)
# =============================================================================

print("\n" + "-"*50)
print("PART 1: lambda (Anonymous Functions)")
print("-"*50)

# --- Example 1: Basic lambda vs def ---
print("\n--- 1. lambda vs def ---")

def square_def(x):
    return x ** 2

square_lambda = lambda x: x ** 2

print(f"Using def: square_def(5) = {square_def(5)}")
print(f"Using lambda: square_lambda(5) = {square_lambda(5)}")

# --- Example 2: Multiple parameters ---
print("\n--- 2. lambda with multiple parameters ---")
add = lambda a, b: a + b
print(f"lambda add(3, 5) = {add(3, 5)}")

# --- Example 3: Using lambda directly (without assigning) ---
print("\n--- 3. lambda passed directly to sorted() ---")
people = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]
sorted_people = sorted(people, key=lambda p: p["age"])
print(f"Sorted by age: {sorted_people}")

# --- Example 4: Ternary inside lambda ---
print("\n--- 4. lambda with ternary operator ---")
max_of_two = lambda a, b: a if a > b else b
print(f"max_of_two(10, 20) = {max_of_two(10, 20)}")


# =============================================================================
# PART 2: map() – Apply Function to Every Element
# =============================================================================

print("\n" + "-"*50)
print("PART 2: map()")
print("-"*50)

# --- Example 1: map with named function ---
print("\n--- 1. map with named function ---")
numbers = [1, 2, 3, 4, 5]

def square(x):
    return x ** 2

squares = list(map(square, numbers))
print(f"Squares using map: {squares}")

# --- Example 2: map with lambda ---
print("\n--- 2. map with lambda ---")
squares_lambda = list(map(lambda x: x ** 2, numbers))
print(f"Squares using map + lambda: {squares_lambda}")

# --- Example 3: map with built-in function ---
print("\n--- 3. map with built-in function ---")
str_nums = ["1", "2", "3", "4"]
int_nums = list(map(int, str_nums))
print(f"Strings to ints: {int_nums}")

# --- Example 4: map with multiple iterables ---
print("\n--- 4. map with multiple iterables ---")
a = [1, 2, 3]
b = [10, 20, 30]
sums = list(map(lambda x, y: x + y, a, b))
print(f"Element-wise sums: {sums}")


# =============================================================================
# PART 3: filter() – Keep Only Items Where Function is True
# =============================================================================

print("\n" + "-"*50)
print("PART 3: filter()")
print("-"*50)

# --- Example 1: filter with named function ---
print("\n--- 1. filter with named function ---")
numbers = [1, 2, 3, 4, 5, 6]

def is_even(x):
    return x % 2 == 0

evens = list(filter(is_even, numbers))
print(f"Evens using filter: {evens}")

# --- Example 2: filter with lambda ---
print("\n--- 2. filter with lambda ---")
evens_lambda = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Evens using filter + lambda: {evens_lambda}")

# --- Example 3: filter with strings ---
print("\n--- 3. filter with strings ---")
words = ["apple", "banana", "cherry", "date"]
long_words = list(filter(lambda w: len(w) > 5, words))
print(f"Words longer than 5 chars: {long_words}")

# --- Example 4: filter with None (removes falsy values) ---
print("\n--- 4. filter with None (removes falsy values) ---")
values = [0, 1, False, 2, "", 3, None, "hello"]
filtered = list(filter(None, values))
print(f"Falsy values removed: {filtered}")


# =============================================================================
# PART 4: Comparison with Comprehensions
# =============================================================================

print("\n" + "-"*50)
print("PART 4: Comparison with Comprehensions")
print("-"*50)

# --- Example 1: map vs list comprehension ---
print("\n--- 1. map vs list comprehension ---")
numbers = [1, 2, 3, 4, 5]

# Using map
squares_map = list(map(lambda x: x ** 2, numbers))

# Using comprehension (preferred)
squares_comp = [x ** 2 for x in numbers]

print(f"map:        {squares_map}")
print(f"comprehension: {squares_comp}")

# --- Example 2: filter vs list comprehension ---
print("\n--- 2. filter vs list comprehension ---")
numbers = [1, 2, 3, 4, 5, 6]

# Using filter
evens_filter = list(filter(lambda x: x % 2 == 0, numbers))

# Using comprehension (preferred)
evens_comp = [x for x in numbers if x % 2 == 0]

print(f"filter:     {evens_filter}")
print(f"comprehension: {evens_comp}")

# --- Example 3: Combining map and filter vs comprehension ---
print("\n--- 3. map + filter vs comprehension ---")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using map and filter together (harder to read)
result_map = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))

# Using comprehension (much clearer)
result_comp = [x ** 2 for x in numbers if x % 2 == 0]

print(f"map + filter: {result_map}")
print(f"comprehension: {result_comp}")


# =============================================================================
# COMMON MISTAKES
# =============================================================================

print("\n" + "-"*50)
print("COMMON MISTAKES TO AVOID")
print("-"*50)

print("""
❌ Mistake 1: Forgetting to convert map/filter to list
   map(lambda x: x**2, numbers)   # Returns map object
   list(map(lambda x: x**2, numbers))  # Correct

❌ Mistake 2: Using lambda for side effects (print, etc.)
   lambda x: print(x)   # Returns None, bad practice
   # Use a normal def function or a for loop.

❌ Mistake 3: Using lambda with multiple statements (impossible)
   lambda x: if x > 0: return x   # SyntaxError
   # Use ternary operator: lambda x: x if x > 0 else -x

❌ Mistake 4: Using map/filter when a comprehension is clearer
   # Unnecessary complexity.
   # Use comprehension for simple transformations.

❌ Mistake 5: Forgetting to import reduce (if using)
   reduce is in functools, not built-in.
   from functools import reduce
""")


# =============================================================================
# CORE EXERCISES (Mastery Check)
# =============================================================================

print("\n" + "="*70)
print("CORE EXERCISES (Mastery Check)")
print("="*70)

print("""
EXERCISE 1 (lambda):
Write a lambda that takes three numbers and returns their product.
Assign it to a variable multiply_three. Test it with (2, 3, 4).

EXERCISE 2 (map):
Given a list of temperatures in Celsius [0, 20, 30, 40],
use map and a lambda to convert them to Fahrenheit
(F = C * 9/5 + 32). Print the result as a list.

EXERCISE 3 (filter):
Given a list of numbers [12, 15, 18, 21, 24, 27],
use filter and a lambda to keep only numbers divisible by 3
AND greater than 20. Print the result as a list.

EXERCISE 4 (Combining):
Given a list of strings ["Hello", "World", "Python", "is", "Fun"],
use map and filter together (or comprehensions) to:
1. Filter out words shorter than 3 characters.
2. Convert the remaining words to uppercase.
3. Print the result as a list.
""")


# =============================================================================
# 📌 ADVANCED EXTENSION (For Wandering)
# =============================================================================

print("\n" + "="*70)
print("ADVANCED EXTENSION (Optional - For Wandering)")
print("="*70)

print("""
The following concepts are EXTRA. They are NOT required for this topic.
Read them if you are curious.
""")

# 1. reduce() from functools
print("\n--- 1. functools.reduce() ---")
from functools import reduce
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(f"Product of numbers using reduce: {product}")

# 2. map with multiple iterables (showcased earlier)
print("\n--- 2. map with more than two iterables ---")
a = [1, 2, 3]
b = [10, 20, 30]
c = [100, 200, 300]
result = list(map(lambda x, y, z: x + y + z, a, b, c))
print(f"Sum of three lists element-wise: {result}")

# 3. filter with lambda for complex conditions
print("\n--- 3. filter with complex condition ---")
data = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 18}, {"name": "Charlie", "age": 25}]
adults = list(filter(lambda p: p["age"] >= 21, data))
print(f"People aged 21 or older: {adults}")

# 4. lambda as a key in sorted (done earlier)
print("\n--- 4. sorted with lambda key ---")
words = ["banana", "apple", "cherry", "date"]
sorted_words = sorted(words, key=lambda w: len(w))
print(f"Words sorted by length: {sorted_words}")

print("\n" + "="*70)
print("END OF HANDOUT #11")
print("="*70)