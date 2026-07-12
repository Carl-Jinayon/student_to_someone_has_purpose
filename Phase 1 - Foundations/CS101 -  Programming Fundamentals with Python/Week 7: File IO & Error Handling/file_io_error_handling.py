#!/usr/bin/env python3
"""
================================================================================
HANDOUT #8: FILE I/O & ERROR HANDLING (Step 8)
================================================================================
Student: ________________________________
Date: ___________________________________

This handout covers:
    1. Opening and closing files (the 'with' statement)
    2. Reading text files (read, readlines, line-by-line)
    3. Writing text files (write, append)
    4. JSON (structured data with lists and dicts)
    5. Error Handling (try / except / else / finally)
    6. Raising custom errors (raise)

Prerequisites used: int, str, bool, print(), containers, control flow, functions.
No advanced topics like decorators or *args are used.
================================================================================
"""

import json
from pathlib import Path

print("\n" + "="*70)
print("STEP 8: FILE I/O & ERROR HANDLING")
print("="*70)

# =============================================================================
# PART 1: Basic File Operations (with statement)
# =============================================================================

print("\n" + "-"*50)
print("PART 1: Reading and Writing Text Files")
print("-"*50)

# --- Writing to a file ---
print("\n--- Writing text (overwrites) ---")
with open("example.txt", "w") as f:
    f.write("Hello, world!\n")
    f.write("This is a second line.\n")
print("Created example.txt with two lines.")

# --- Reading from a file ---
print("\n--- Reading entire file ---")
with open("example.txt", "r") as f:
    content = f.read()
print(f"Content:\n{content}")

# --- Reading line by line (memory-efficient for large files) ---
print("\n--- Reading line by line ---")
with open("example.txt", "r") as f:
    for line in f:
        print(f"Line: {line.strip()}")  # strip() removes the \n

# --- Appending to a file (adds to the end) ---
print("\n--- Appending text ---")
with open("example.txt", "a") as f:
    f.write("This line was appended.\n")
print("Appended a third line.")

with open("example.txt", "r") as f:
    print(f"After append:\n{f.read()}")

# --- Reading all lines into a list ---
print("\n--- readlines() -> list of strings ---")
with open("example.txt", "r") as f:
    lines = f.readlines()
print(f"Lines list: {lines}")


# =============================================================================
# PART 2: Working with JSON (Structured Data)
# =============================================================================

print("\n" + "-"*50)
print("PART 2: JSON (Structured Data - Lists and Dicts)")
print("-"*50)

# --- Writing a dictionary to JSON ---
print("\n--- Writing dict to JSON ---")
data = {"name": "Alice", "age": 30, "city": "Manila"}
with open("person.json", "w") as f:
    json.dump(data, f, indent=2)   # indent makes it human-readable
print("Created person.json")

# --- Reading a dictionary from JSON ---
print("\n--- Reading dict from JSON ---")
with open("person.json", "r") as f:
    loaded_data = json.load(f)
print(f"Loaded: {loaded_data}")
print(f"Name: {loaded_data['name']}")

# --- JSON with a list of dictionaries ---
print("\n--- JSON with list of objects ---")
people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]
with open("people.json", "w") as f:
    json.dump(people, f, indent=2)

with open("people.json", "r") as f:
    loaded_people = json.load(f)

total_age = 0
for person in loaded_people:
    total_age = total_age + person["age"]
print(f"Total age of all people: {total_age}")


# =============================================================================
# PART 3: Error Handling (try / except / else / finally)
# =============================================================================

print("\n" + "-"*50)
print("PART 3: Error Handling (try/except)")
print("-"*50)

# --- Example 1: File not found ---
print("\n--- Example 1: Handling FileNotFoundError ---")
try:
    with open("missing_file.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("Error: File not found. Creating it now.")
    with open("missing_file.txt", "w") as f:
        f.write("File was created automatically.")

# --- Example 2: Safe division with multiple errors ---
print("\n--- Example 2: Safe division ---")
def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None
    except TypeError:
        print("Error: Both arguments must be numbers.")
        return None
    else:
        print("Division successful.")
        return result
    finally:
        print("  (safe_divide finished running)")

print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_divide(10, "hello"))

# --- Example 3: Input validation with try/except ---
print("\n--- Example 3: Input validation ---")
def get_number():
    try:
        value = int(input("Enter a number: "))
        return value
    except ValueError:
        print("That's not a valid number!")
        return None

# Uncomment to test:
# num = get_number()
# if num is not None:
#     print(f"You entered: {num}")


# =============================================================================
# PART 4: Raising Custom Errors (raise)
# =============================================================================

print("\n" + "-"*50)
print("PART 4: Raising Custom Errors")
print("-"*50)

def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    if age > 150:
        raise ValueError("Age cannot be over 150.")
    return True

print("\n--- Validating age ---")
try:
    validate_age(25)
    print("Age is valid.")
except ValueError as e:
    print(f"Validation failed: {e}")

try:
    validate_age(-5)
except ValueError as e:
    print(f"Validation failed: {e}")


# =============================================================================
# PART 5: pathlib – Modern Path Handling (Preview)
# =============================================================================

print("\n" + "-"*50)
print("PART 5: pathlib (Modern Paths)")
print("-"*50)

# pathlib is the modern way to work with file paths.
# It works on Windows, Mac, and Linux without changing code.

# Create a Path object
path = Path("data")
path.mkdir(exist_ok=True)   # Create directory if it doesn't exist

# Join paths using /
file_path = path / "note.txt"
file_path.write_text("Hello from pathlib!")
print(f"Wrote to: {file_path}")

# Read it back
content = file_path.read_text()
print(f"Content: {content}")

# List files in the directory
print("\nFiles in 'data' directory:")
for p in path.iterdir():
    print(f"  {p.name}")


# =============================================================================
# COMMON MISTAKES (Step 8 Edition)
# =============================================================================

print("\n" + "-"*50)
print("COMMON MISTAKES TO AVOID")
print("-"*50)

print("""
❌ Mistake 1: Forgetting to close a file (without 'with')
   file = open("file.txt", "r")
   content = file.read()
   # file.close() missing -> resource leak

   Fix: Always use `with open(...) as f:`

❌ Mistake 2: Using "w" mode when you meant "a"
   open("file.txt", "w") OVERWRITES the entire file.

   Fix: Use "a" (append) to add to the end.

❌ Mistake 3: Reading a file that doesn't exist (no try/except)
   open("missing.txt", "r") -> FileNotFoundError

   Fix: Wrap in try/except.

❌ Mistake 4: Not using encoding
   open("file.txt", "r") can fail on non-UTF-8 files.

   Fix: open("file.txt", "r", encoding="utf-8")

❌ Mistake 5: Bare except clause (hides ALL errors)
   try:
       ...
   except:   # Swallows KeyboardInterrupt, MemoryError, etc.
       pass

   Fix: except SpecificError: or except Exception as e:

❌ Mistake 6: Using json.load on a non-JSON file
   Fails with JSONDecodeError.

   Fix: Handle the error, or ensure the file exists.
""")


# =============================================================================
# CORE EXERCISES (Step 8 Mastery Check)
# =============================================================================

print("\n" + "="*70)
print("CORE EXERCISES (Step 8 Mastery Check)")
print("="*70)

print("""
EXERCISE 1 (Write and Read):
Write a program that:
1. Asks the user for their name and age.
2. Writes this data to a file called user_data.txt
   in the format: "Name: Alice, Age: 30".
3. Reads the file back and prints the content.

EXERCISE 2 (JSON):
Write a program that:
1. Creates a list of dictionaries, each representing a product:
   {"id": 1, "name": "Laptop", "price": 999.99}
2. Writes this list to products.json.
3. Reads the JSON file and prints the total price of all products.

EXERCISE 3 (Error Handling):
Write a function safe_divide(a, b) that:
1. Tries to divide a by b.
2. Returns the result if successful.
3. Handles ZeroDivisionError by printing "Cannot divide by zero"
   and returning None.
4. Handles TypeError by printing "Invalid type" and returning None.

EXERCISE 4 (File with Error Handling):
Write a program that:
1. Asks the user for a filename.
2. Tries to open and read the file.
3. If the file doesn't exist, prints "File not found" and creates
   an empty file with that name.
4. If the file exists, prints its content.
""")


# =============================================================================
# 📌 ADVANCED EXTENSION (Optional - For Wandering)
# =============================================================================

print("\n" + "="*70)
print("ADVANCED EXTENSION (Optional - For Wandering)")
print("="*70)

print("""
The following concepts are EXTRA. They are NOT required for Step 8 mastery.
Read them if you are curious.
""")

# 1. CSV Module (spreadsheet data)
print("\n--- 1. CSV Module ---")
import csv

data = [["Name", "Age"], ["Alice", 30], ["Bob", 25]]
with open("people.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)

with open("people.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(f"  {row}")

# 2. Full try/except/else/finally example
print("\n--- 2. try/except/else/finally ---")
def process_file(filename):
    try:
        with open(filename, "r") as f:
            data = f.read()
    except FileNotFoundError:
        print(f"  File {filename} not found.")
        return None
    except PermissionError:
        print(f"  Permission denied for {filename}.")
        return None
    else:
        print(f"  File read successfully.")
        return data
    finally:
        print(f"  Finished processing {filename}.")

process_file("example.txt")
process_file("does_not_exist.txt")

# 3. Multiple exceptions in one except
print("\n--- 3. Multiple exceptions in one except ---")
try:
    x = int(input("Enter a number: "))
    result = 10 / x
except (ValueError, ZeroDivisionError) as e:
    print(f"  Error: {e}")
else:
    print(f"  Result: {result}")

# 4. Custom Exception Class (advanced)
print("\n--- 4. Custom Exception Class ---")
class NegativeNumberError(Exception):
    pass

def square_root(x):
    if x < 0:
        raise NegativeNumberError("Cannot take square root of negative number")
    return x ** 0.5

try:
    print(square_root(9))
    print(square_root(-1))
except NegativeNumberError as e:
    print(f"  Custom error caught: {e}")

# 5. Reading binary files (preview)
print("\n--- 5. Binary files (preview) ---")
with open("example.txt", "rb") as f:  # 'rb' = read binary
    binary_data = f.read()
    print(f"  First 10 bytes: {binary_data[:10]}")

print("\n" + "="*70)
print("END OF HANDOUT #8")
print("="*70)