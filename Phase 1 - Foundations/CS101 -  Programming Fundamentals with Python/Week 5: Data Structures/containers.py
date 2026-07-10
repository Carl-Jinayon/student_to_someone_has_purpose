#!/usr/bin/env python3
"""
================================================================================
HANDOUT #7: CONTAINERS (Step 7)
================================================================================
Student: ________________________________
Date: ___________________________________

This handout covers:
    1. Lists (mutable, ordered sequences)
    2. Tuples (immutable, ordered sequences)
    3. Dictionaries (key-value mappings)
    4. Sets (unique, unordered collections)

Prerequisites used: int, str, bool, print(), operators, control flow, functions.
================================================================================
"""

print("\n" + "="*70)
print("STEP 7: CONTAINERS")
print("="*70)

# =============================================================================
# PART 1: LIST
# =============================================================================

print("\n" + "-"*50)
print("PART 1: LIST")
print("-"*50)

# --- Creation ---
print("\n--- Creation ---")
empty = []
numbers = [10, 20, 30, 40]
mixed = [1, "hello", 3.14, True]
print(f"numbers: {numbers}")
print(f"mixed: {mixed}")

# --- Access ---
print("\n--- Access ---")
print(f"numbers[0] -> {numbers[0]}")
print(f"numbers[-1] -> {numbers[-1]}")        # Last
print(f"numbers[1:3] -> {numbers[1:3]}")      # Slice (stop exclusive)
print(f"numbers[::2] -> {numbers[::2]}")      # Every second

# --- Mutation ---
print("\n--- Mutation ---")
fruits = ["apple", "banana"]
print(f"Initial: {fruits}")

fruits.append("cherry")
print(f"After append: {fruits}")

fruits.insert(1, "blueberry")
print(f"After insert: {fruits}")

last = fruits.pop()
print(f"Popped: {last}, after pop: {fruits}")

fruits.remove("banana")
print(f"After remove: {fruits}")

fruits[1] = "blackberry"
print(f"After assignment: {fruits}")

print(f"Length: {len(fruits)}")

# --- Looping ---
print("\n--- Looping over a list ---")
fruits = ["apple", "banana", "cherry"]
print("Direct iteration:")
for fruit in fruits:
    print(f"  {fruit}")

print("With index:")
for i in range(len(fruits)):
    print(f"  {i}: {fruits[i]}")


# =============================================================================
# PART 2: TUPLE
# =============================================================================

print("\n" + "-"*50)
print("PART 2: TUPLE")
print("-"*50)

# --- Creation ---
print("\n--- Creation ---")
empty = ()
coords = (10, 20)
single = (5,)        # REQUIRES trailing comma
point = 30, 40       # Parentheses optional
print(f"coords: {coords}, type: {type(coords)}")
print(f"single: {single}, type: {type(single)}")

# --- Access (same as list, but cannot change) ---
print("\n--- Access ---")
print(f"coords[0] -> {coords[0]}")
print(f"coords[-1] -> {coords[-1]}")

# --- Unpacking ---
print("\n--- Unpacking ---")
x, y = coords
print(f"Unpacked: x={x}, y={y}")

# --- Attempting to mutate (error) ---
print("\n--- Immutability ---")
try:
    coords[0] = 99
except TypeError as e:
    print(f"❌ Cannot change tuple: {e}")

# --- When to use ---
print("\nUse tuples for fixed data that should never change.")
print("Example: coordinates, RGB values, database row records.")


# =============================================================================
# PART 3: DICTIONARY
# =============================================================================

print("\n" + "-"*50)
print("PART 3: DICTIONARY")
print("-"*50)

# --- Creation ---
print("\n--- Creation ---")
empty = {}
person = {
    "name": "Alice",
    "age": 30,
    "city": "Manila"
}
print(f"person: {person}")

# --- Access ---
print("\n--- Access ---")
print(f"person['name'] -> {person['name']}")
print(f"person.get('age') -> {person.get('age')}")        # None if missing
print(f"person.get('country', 'unknown') -> {person.get('country', 'unknown')}")

# --- Mutation (Add, Update, Delete) ---
print("\n--- Mutation ---")
person["age"] = 31        # Update
person["job"] = "Engineer" # Add
print(f"After update/add: {person}")

del person["city"]
print(f"After deleting city: {person}")

# --- Looping ---
print("\n--- Looping over dict ---")
person = {"name": "Alice", "age": 30, "city": "Manila"}

print("Over keys:")
for key in person:
    print(f"  {key}: {person[key]}")

print("Over items (key, value):")
for key, value in person.items():
    print(f"  {key} = {value}")

print("Over keys only:")
for key in person.keys():
    print(f"  {key}")

print("Over values only:")
for value in person.values():
    print(f"  {value}")


# =============================================================================
# PART 4: SET
# =============================================================================

print("\n" + "-"*50)
print("PART 4: SET")
print("-"*50)

# --- Creation ---
print("\n--- Creation ---")
empty = set()        # MUST use set() - {} is dict
numbers = {1, 2, 3, 3, 3}   # Duplicates removed -> {1,2,3}
mixed = {1, "hello", 3.14}
print(f"numbers: {numbers}")
print(f"mixed: {mixed}")

# --- Add and Remove ---
print("\n--- Add and Remove ---")
s = {1, 2, 3}
print(f"Initial: {s}")

s.add(4)
print(f"After add(4): {s}")

s.remove(2)
print(f"After remove(2): {s}")

s.discard(5)   # No error if missing
print(f"After discard(5): {s}")

# --- Membership (fast) ---
print("\n--- Membership ---")
print(f"3 in s? {3 in s}")
print(f"5 in s? {5 in s}")

# --- Set Operations ---
print("\n--- Set Operations ---")
a = {1, 2, 3}
b = {3, 4, 5}
print(f"a: {a}, b: {b}")
print(f"Union (a | b): {a | b}")
print(f"Intersection (a & b): {a & b}")
print(f"Difference (a - b): {a - b}")
print(f"Symmetric diff (a ^ b): {a ^ b}")

# --- Looping ---
print("\n--- Looping over set ---")
for value in {1, 2, 3}:
    print(f"  {value}")   # Order is NOT guaranteed


# =============================================================================
# COMMON MISTAKES
# =============================================================================

print("\n" + "-"*50)
print("COMMON MISTAKES TO AVOID")
print("-"*50)

print("\n❌ Mistake 1: {} for empty set")
print("   # empty = {}   # This is a dict")
print("   empty = set()  # Correct")

print("\n❌ Mistake 2: Using list as dict key")
print("   # d = {[1,2]: 'value'}  # TypeError")
print("   d = {(1,2): 'value'}    # Correct (use tuple)")

print("\n❌ Mistake 3: Modifying list while iterating")
print("   # for x in lst:")
print("   #     if x < 0: lst.remove(x)  # Problematic")
print("   # for x in list(lst):  # Iterate over a copy")

print("\n❌ Mistake 4: Forgetting trailing comma in 1-element tuple")
print("   # t = (5)   # This is int")
print("   t = (5,)    # This is tuple")

print("\n❌ Mistake 5: Direct dict access without get()")
print("   # person['country']  # KeyError if missing")
print("   person.get('country', 'unknown')  # Safe")


# =============================================================================
# CORE EXERCISES
# =============================================================================

print("\n" + "="*70)
print("CORE EXERCISES (Step 7 Mastery Check)")
print("="*70)

print("""
EXERCISE 1 (List):
Write a function average_list(numbers) that takes a list of numbers
and returns their average. Test with [10, 20, 30, 40].

EXERCISE 2 (Tuple):
Write a function min_max_tuple(data) that takes a list of numbers
and returns a tuple (min, max). Test with [5, 2, 8, 1, 9].

EXERCISE 3 (Dict):
Write a function char_count(text) that takes a string and returns a
dictionary with the count of each character. Test with "hello".

EXERCISE 4 (Set):
Write a function common_elements(list1, list2) that returns a set
of elements common to both lists. Test with [1,2,3,4] and [3,4,5,6].

EXERCISE 5 (Combining):
Write a function unique_values(data) that takes a list and returns a
list of unique values, keeping the order of first appearance.
(Hint: Use a set to track seen values.)
""")


# =============================================================================
# 📌 ADVANCED EXTENSION (Optional - For Wandering)
# =============================================================================

print("\n" + "="*70)
print("ADVANCED EXTENSION (Optional - For Wandering)")
print("="*70)

print("""
The following concepts are EXTRA. They are NOT required for Step 7 mastery.
Read them if you are curious.
""")

# 1. List Comprehension
print("\n--- 1. List Comprehension ---")
squares = [x**2 for x in range(5)]
evens = [x for x in range(10) if x % 2 == 0]
print(f"Squares: {squares}")
print(f"Evens: {evens}")

# 2. Dict Comprehension
print("\n--- 2. Dict Comprehension ---")
squares_dict = {x: x**2 for x in range(5)}
print(f"Squares dict: {squares_dict}")

# 3. enumerate()
print("\n--- 3. enumerate() ---")
fruits = ["apple", "banana", "cherry"]
for idx, fruit in enumerate(fruits):
    print(f"  {idx}: {fruit}")

# 4. zip()
print("\n--- 4. zip() ---")
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"  {name} is {age} years old.")

# 5. Set Comprehension
print("\n--- 5. Set Comprehension ---")
squares_set = {x**2 for x in range(5)}
print(f"Squares set: {squares_set}")

# 6. Sorting lists (just a preview)
print("\n--- 6. Sorting (preview) ---")
unsorted = [3, 1, 4, 1, 5]
sorted_list = sorted(unsorted)   # returns a new sorted list
print(f"Sorted: {sorted_list}")
unsorted.sort()                  # sorts in place
print(f"In-place sort: {unsorted}")

# 7. Copying lists (shallow copy)
print("\n--- 7. Copying (preview) ---")
original = [1, 2, 3]
shallow_copy = original.copy()
shallow_copy.append(4)
print(f"Original: {original}")
print(f"Copy: {shallow_copy}")

print("\n" + "="*70)
print("END OF HANDOUT #7")
print("="*70)