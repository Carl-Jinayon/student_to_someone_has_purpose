#!/usr/bin/env python3
"""
================================================================================
HANDOUT #12: ZIP AND ENUMERATE (Mastery Week – Topic 3)
================================================================================
Student: ________________________________
Date: ___________________________________

This handout covers:
    1. enumerate() – Get index and value in a loop
    2. zip() – Loop over multiple lists in parallel
    3. Combining enumerate and zip
    4. Comparison with range(len())

Prerequisites used: Loops, Lists, Tuples, Dicts.
================================================================================
"""

print("\n" + "="*70)
print("MASTERY WEEK – TOPIC 3: ZIP AND ENUMERATE")
print("="*70)

# =============================================================================
# PART 1: enumerate() – Index and Value
# =============================================================================

print("\n" + "-"*50)
print("PART 1: enumerate()")
print("-"*50)

# --- Example 1: Basic enumerate ---
print("\n--- 1. Basic enumerate ---")
fruits = ["apple", "banana", "cherry"]

# Ugly way (without enumerate)
print("Ugly way (range(len())):")
for i in range(len(fruits)):
    print(f"  {i}: {fruits[i]}")

# Pythonic way (with enumerate)
print("\nPythonic way (enumerate):")
for index, fruit in enumerate(fruits):
    print(f"  {index}: {fruit}")

# --- Example 2: enumerate with start=1 ---
print("\n--- 2. enumerate with start=1 ---")
tasks = ["Buy groceries", "Clean room", "Study Python"]
print("To-do list:")
for num, task in enumerate(tasks, start=1):
    print(f"  {num}. {task}")

# --- Example 3: enumerate with strings ---
print("\n--- 3. enumerate with strings ---")
word = "hello"
for idx, char in enumerate(word):
    print(f"  Character at position {idx}: {char}")


# =============================================================================
# PART 2: zip() – Loop Over Multiple Lists in Parallel
# =============================================================================

print("\n" + "-"*50)
print("PART 2: zip()")
print("-"*50)

# --- Example 1: Basic zip with two lists ---
print("\n--- 1. Basic zip with two lists ---")
names = ["Alice", "Bob", "Charlie"]
scores = [95, 87, 92]

# Ugly way (without zip)
print("Ugly way (range(len())):")
for i in range(len(names)):
    print(f"  {names[i]}: {scores[i]}")

# Pythonic way (with zip)
print("\nPythonic way (zip):")
for name, score in zip(names, scores):
    print(f"  {name}: {score}")

# --- Example 2: zip with three lists ---
print("\n--- 2. zip with three lists ---")
students = ["Alice", "Bob", "Charlie"]
subjects = ["Math", "Science", "English"]
grades = [95, 87, 92]

for student, subject, grade in zip(students, subjects, grades):
    print(f"  {student} scored {grade} in {subject}")

# --- Example 3: zip stops at the shortest list ---
print("\n--- 3. zip stops at the shortest list ---")
a = [1, 2, 3, 4]
b = [10, 20]
print(f"zip({a}, {b}):")
for x, y in zip(a, b):
    print(f"  {x} {y}")
print("  (3 and 4 are lost because b is shorter)")

# --- Example 4: zip to list of tuples ---
print("\n--- 4. zip to list of tuples ---")
pairs = list(zip(names, scores))
print(f"List of tuples: {pairs}")

# --- Example 5: zip to dictionary ---
print("\n--- 5. zip to dictionary ---")
keys = ["name", "age", "city"]
values = ["Alice", 30, "Manila"]
person = dict(zip(keys, values))
print(f"Dictionary from zip: {person}")


# =============================================================================
# PART 3: Combining enumerate and zip
# =============================================================================

print("\n" + "-"*50)
print("PART 3: Combining enumerate and zip")
print("-"*50)

# --- Example 1: Numbered list with paired data ---
print("\n--- 1. Numbered list with paired data ---")
names = ["Alice", "Bob", "Charlie"]
scores = [95, 87, 92]

for idx, (name, score) in enumerate(zip(names, scores), start=1):
    print(f"  {idx}. {name} scored {score}")

# --- Example 2: Products with prices ---
print("\n--- 2. Products with prices ---")
products = ["Laptop", "Mouse", "Keyboard"]
prices = [999.99, 25.50, 75.00]

for num, (product, price) in enumerate(zip(products, prices), start=1):
    print(f"  {num}. {product} - ${price:.2f}")


# =============================================================================
# PART 4: Comparison with range(len())
# =============================================================================

print("\n" + "-"*50)
print("PART 4: Comparison with range(len())")
print("-"*50)

names = ["Alice", "Bob", "Charlie", "Diana"]
ages = [30, 25, 35, 28]

# Ugly way: range(len())
print("Ugly way (range(len())):")
for i in range(len(names)):
    print(f"  {names[i]} is {ages[i]} years old.")

# Pythonic way: zip + enumerate
print("\nPythonic way (zip + enumerate):")
for idx, (name, age) in enumerate(zip(names, ages), start=1):
    print(f"  {idx}. {name} is {age} years old.")


# =============================================================================
# COMMON MISTAKES
# =============================================================================

print("\n" + "-"*50)
print("COMMON MISTAKES TO AVOID")
print("-"*50)

print("""
❌ Mistake 1: Using range(len()) instead of enumerate
   for i in range(len(lst)): print(lst[i])  # Bad
   for i, val in enumerate(lst): print(i, val)  # Good

❌ Mistake 2: Forgetting to unpack enumerate's two values
   for item in enumerate(lst):  # item is a tuple (idx, value)
   # Fix: for idx, val in enumerate(lst):

❌ Mistake 3: Forgetting that zip truncates to the shortest list
   zip([1,2,3,4], [10,20])  # Only yields two pairs
   # Fix: Use itertools.zip_longest if you need all elements.

❌ Mistake 4: Using zip on dictionaries (zips keys, not values)
   zip(dict1, dict2)  # zips keys
   # Fix: zip(dict1.values(), dict2.values()) or .items()

❌ Mistake 5: Not converting zip to list for debugging
   print(zip(a, b))  # Prints <zip object at ...>
   # Fix: print(list(zip(a, b)))
""")


# =============================================================================
# CORE EXERCISES (Mastery Check)
# =============================================================================

print("\n" + "="*70)
print("CORE EXERCISES (Mastery Check)")
print("="*70)

print("""
EXERCISE 1 (enumerate with start):
Given a list of tasks ["Buy groceries", "Clean room", "Study Python"],
use enumerate to print them as a numbered to-do list starting from 1.
Output should be:
1. Buy groceries
2. Clean room
3. Study Python

EXERCISE 2 (zip with three lists):
Given three lists:
students = ["Alice", "Bob", "Charlie"]
subjects = ["Math", "Science", "English"]
grades = [95, 87, 92]
Use zip to print each student's grade in their subject:
"Alice scored 95 in Math"

EXERCISE 3 (zip to dictionary):
Given two lists:
keys = ["id", "name", "age"]
values = [101, "Alice", 30]
Use zip and dict() to create a dictionary and print it.

EXERCISE 4 (Combined enumerate + zip):
Given two lists:
products = ["Laptop", "Mouse", "Keyboard"]
prices = [999.99, 25.50, 75.00]
Use enumerate and zip together to print a numbered list of
products with prices, formatted as:
1. Laptop - $999.99
2. Mouse - $25.50
3. Keyboard - $75.00
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

# 1. itertools.zip_longest
print("\n--- 1. itertools.zip_longest ---")
from itertools import zip_longest
a = [1, 2, 3, 4]
b = [10, 20]
print("zip_longest with fillvalue=0:")
for x, y in zip_longest(a, b, fillvalue=0):
    print(f"  {x} {y}")

# 2. enumerate on dictionary (iterates over keys)
print("\n--- 2. enumerate on dictionary ---")
person = {"name": "Alice", "age": 30, "city": "Manila"}
for idx, key in enumerate(person):
    print(f"  {idx}: {key} -> {person[key]}")

# 3. Unzipping with zip(*)
print("\n--- 3. Unzipping with zip(*) ---")
pairs = [("Alice", 95), ("Bob", 87), ("Charlie", 92)]
names, scores = zip(*pairs)
print(f"Names: {names}")
print(f"Scores: {scores}")

# 4. zip with list comprehension
print("\n--- 4. zip with list comprehension ---")
names = ["Alice", "Bob", "Charlie"]
scores = [95, 87, 92]
formatted = [f"{name} scored {score}" for name, score in zip(names, scores)]
print(f"Formatted strings: {formatted}")

# 5. zip with more than 3 iterables
print("\n--- 5. zip with 4 iterables ---")
a = [1, 2, 3]
b = [10, 20, 30]
c = [100, 200, 300]
d = [1000, 2000, 3000]
for x, y, z, w in zip(a, b, c, d):
    print(f"  {x} + {y} + {z} + {w} = {x + y + z + w}")

print("\n" + "="*70)
print("END OF HANDOUT #12")
print("="*70)