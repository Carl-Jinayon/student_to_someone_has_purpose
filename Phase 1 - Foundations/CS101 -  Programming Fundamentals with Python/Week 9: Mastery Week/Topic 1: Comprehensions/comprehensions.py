#!/usr/bin/env python3
"""
================================================================================
HANDOUT #10: COMPREHENSIONS (Mastery Week – Topic 1)
================================================================================
Student: ________________________________
Date: ___________________________________

This handout covers:
    1. List Comprehensions
    2. Dict Comprehensions
    3. Set Comprehensions
    4. When to use (and when NOT to use)

Prerequisites used: Loops, Conditionals, Lists, Dicts, Sets.
================================================================================
"""

print("\n" + "="*70)
print("MASTERY WEEK – TOPIC 1: COMPREHENSIONS")
print("="*70)

# =============================================================================
# PART 1: List Comprehensions
# =============================================================================

print("\n" + "-"*50)
print("PART 1: List Comprehensions")
print("-"*50)

# --- Example 1: Squares of numbers ---
print("\n--- 1. Squares of numbers ---")
numbers = [1, 2, 3, 4, 5]

# Long-form
squares_long = []
for x in numbers:
    squares_long.append(x**2)
print(f"Long-form: {squares_long}")

# Comprehension
squares = [x**2 for x in numbers]
print(f"Comprehension: {squares}")

# --- Example 2: Filtering (even numbers) ---
print("\n--- 2. Filtering (even numbers) ---")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [x for x in numbers if x % 2 == 0]
print(f"Evens: {evens}")

# --- Example 3: Squares of even numbers ---
print("\n--- 3. Squares of even numbers ---")
even_squares = [x**2 for x in numbers if x % 2 == 0]
print(f"Even squares: {even_squares}")

# --- Example 4: Strings (uppercase and filter) ---
print("\n--- 4. Strings (uppercase, filter by length) ---")
words = ["apple", "banana", "cherry", "date", "elderberry"]
uppercase_long = [word.upper() for word in words if len(word) > 5]
print(f"Uppercase words longer than 5 chars: {uppercase_long}")


# =============================================================================
# PART 2: Dict Comprehensions
# =============================================================================

print("\n" + "-"*50)
print("PART 2: Dict Comprehensions")
print("-"*50)

# --- Example 1: Mapping numbers to squares ---
print("\n--- 1. Mapping numbers to squares ---")
squares_dict = {x: x**2 for x in range(5)}
print(f"Squares dict: {squares_dict}")

# --- Example 2: Filtering a dictionary ---
print("\n--- 2. Filtering a dictionary ---")
original = {"Alice": 25, "Bob": 30, "Charlie": 18, "Diana": 27}
filtered = {name: age for name, age in original.items() if age > 20}
print(f"People over 20: {filtered}")

# --- Example 3: Swapping keys and values ---
print("\n--- 3. Swapping keys and values ---")
original = {"a": 1, "b": 2, "c": 3}
swapped = {value: key for key, value in original.items()}
print(f"Swapped: {swapped}")

# --- Example 4: Building a dict from a list of dictionaries ---
print("\n--- 4. Building a dict from a list of dictionaries ---")
books = [
    {"title": "1984", "author": "Orwell"},
    {"title": "Brave New World", "author": "Huxley"}
]
title_to_author = {book["title"]: book["author"] for book in books}
print(f"Title -> Author: {title_to_author}")


# =============================================================================
# PART 3: Set Comprehensions
# =============================================================================

print("\n" + "-"*50)
print("PART 3: Set Comprehensions")
print("-"*50)

# --- Example 1: Unique squares ---
print("\n--- 1. Unique squares ---")
numbers = [1, 2, 2, 3, 3, 3]
unique_squares = {x**2 for x in numbers}
print(f"Unique squares: {unique_squares}")

# --- Example 2: Unique first letters ---
print("\n--- 2. Unique first letters ---")
words = ["apple", "banana", "cherry", "date"]
first_letters = {word[0] for word in words}
print(f"First letters: {first_letters}")

# --- Example 3: Unique vowels in a sentence ---
print("\n--- 3. Unique vowels in a sentence ---")
sentence = "hello world"
vowels = {"a", "e", "i", "o", "u"}
unique_vowels = {char for char in sentence if char in vowels}
print(f"Unique vowels in 'hello world': {unique_vowels}")


# =============================================================================
# PART 4: When to Use vs When NOT to Use
# =============================================================================

print("\n" + "-"*50)
print("PART 4: When to Use (and When NOT to)")
print("-"*50)

print("""
✅ USE comprehensions for:
   - Building a new list/dict/set from an existing one.
   - Simple transformation (one expression).
   - Filtering with a single condition.
   - Readable, concise code.

❌ AVOID comprehensions for:
   - More than one if condition (use nested loops).
   - Side effects (e.g., print(), modifying the original).
   - Complex logic (> 3 lines).
   - Nested comprehensions (can become unreadable).
""")


# =============================================================================
# COMMON MISTAKES
# =============================================================================

print("\n" + "-"*50)
print("COMMON MISTAKES TO AVOID")
print("-"*50)

print("""
❌ Mistake 1: Forgetting the square brackets
   # x for x in range(5)  # Invalid
   [x for x in range(5)]  # Correct

❌ Mistake 2: Using {} for set comprehension incorrectly
   {x: x**2 for x in range(5)}  # Dict comprehension (has colon)
   {x**2 for x in range(5)}     # Set comprehension (no colon)

❌ Mistake 3: Overcomplicating with nested comprehensions
   [x for y in matrix for x in y]  # Hard to read
   # Use nested for loops instead.

❌ Mistake 4: Using comprehensions for side effects
   [print(x) for x in range(5)]  # Creates list of None
   # Use a normal for loop.

❌ Mistake 5: Forgetting the 'if' condition placement
   [x if x > 0 for x in range(5)]  # Invalid
   [x for x in range(5) if x > 0]  # Correct
""")


# =============================================================================
# CORE EXERCISES (Mastery Check)
# =============================================================================

print("\n" + "="*70)
print("CORE EXERCISES (Mastery Check)")
print("="*70)

print("""
EXERCISE 1 (List Comprehension):
Given a list of numbers [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
use a list comprehension to create a new list containing only
the odd numbers squared.

EXERCISE 2 (List Comprehension with Strings):
Given a list of words ["apple", "banana", "cherry", "date", "elderberry"],
use a list comprehension to create a list of words that contain
the letter "a", converted to uppercase.

EXERCISE 3 (Dict Comprehension):
Given a list of dictionaries:
books = [{"title": "1984", "author": "Orwell"},
         {"title": "Brave New World", "author": "Huxley"}]
Use a dict comprehension to create a new dictionary mapping "title" to "author".

EXERCISE 4 (Set Comprehension):
Given a list of numbers [1, 2, 2, 3, 4, 4, 5, 5, 5],
use a set comprehension to create a set of their cubes.
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

# 1. Nested Comprehensions
print("\n--- 1. Nested Comprehensions ---")
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(f"Flattened matrix: {flattened}")

# 2. Ternary Expression Inside Comprehension
print("\n--- 2. Ternary Expression Inside Comprehension ---")
numbers = [1, 2, 3, 4, 5]
result = [x if x > 2 else 0 for x in numbers]
print(f"Numbers > 2 kept, others replaced with 0: {result}")

# 3. Dict Comprehension with zip()
print("\n--- 3. Dict Comprehension with zip() ---")
keys = ["name", "age", "city"]
values = ["Alice", 30, "Manila"]
person = {k: v for k, v in zip(keys, values)}
print(f"Dict from zip(): {person}")

print("\n" + "="*70)
print("END OF HANDOUT #10")
print("="*70)