#!/usr/bin/env python3
"""
================================================================================
HANDOUT #14: os AND sys MODULES (Mastery Week – Topic 5)
================================================================================
Student: ________________________________
Date: ___________________________________

This handout covers:
    1. os.path (cross-platform paths, existence checks)
    2. os (directories, files, environment variables)
    3. sys.argv (command-line arguments)
    4. sys.exit (exit the program)
    5. sys.platform, sys.version

Prerequisites used: All previous steps.
================================================================================
"""

import os
import sys
import json

print("\n" + "="*70)
print("MASTERY WEEK – TOPIC 5: os AND sys MODULES")
print("="*70)

# =============================================================================
# PART 1: os.path – Cross-Platform Paths
# =============================================================================

print("\n" + "-"*50)
print("PART 1: os.path – Cross-Platform Paths")
print("-"*50)

# --- Example 1: Joining paths ---
print("\n--- 1. os.path.join() ---")
path = os.path.join("folder", "subfolder", "file.txt")
print(f"Joined path: {path}")

# --- Example 2: Checking existence ---
print("\n--- 2. os.path.exists() ---")
print(f"Does 'handout_14_os_sys.py' exist? {os.path.exists('handout_14_os_sys.py')}")
print(f"Does 'nonexistent.txt' exist? {os.path.exists('nonexistent.txt')}")

# --- Example 3: Check if file or directory ---
print("\n--- 3. os.path.isfile() and os.path.isdir() ---")
print(f"Is this file a file? {os.path.isfile('handout_14_os_sys.py')}")
print(f"Is this file a directory? {os.path.isdir('handout_14_os_sys.py')}")
print(f"Is '.' a directory? {os.path.isdir('.')}")

# --- Example 4: os.path.basename and dirname ---
print("\n--- 4. os.path.basename() and os.path.dirname() ---")
full_path = os.path.join("folder", "subfolder", "file.txt")
print(f"Full path: {full_path}")
print(f"Directory name: {os.path.dirname(full_path)}")
print(f"Base name: {os.path.basename(full_path)}")

# --- Example 5: Splitting name and extension ---
print("\n--- 5. os.path.splitext() ---")
name, ext = os.path.splitext("file.txt")
print(f"Name: {name}, Extension: {ext}")

# --- Example 6: Absolute path ---
print("\n--- 6. os.path.abspath() ---")
print(f"Absolute path: {os.path.abspath('handout_14_os_sys.py')}")

# --- Example 7: Current working directory ---
print("\n--- 7. os.getcwd() ---")
print(f"Current directory: {os.getcwd()}")


# =============================================================================
# PART 2: os – Directories, Files, Environment Variables
# =============================================================================

print("\n" + "-"*50)
print("PART 2: os – Directories, Files, Environment")
print("-"*50)

# --- Example 1: Listing directory contents ---
print("\n--- 1. os.listdir() ---")
print("First 5 items in current directory:")
for item in os.listdir(".")[:5]:
    print(f"  {item}")

# --- Example 2: Creating directories ---
print("\n--- 2. os.makedirs() ---")
os.makedirs("test_dir/nested", exist_ok=True)
print("Created test_dir/nested/")

# --- Example 3: Environment variables ---
print("\n--- 3. os.environ.get() ---")
python_path = os.environ.get("PYTHONPATH", "Not set")
print(f"PYTHONPATH: {python_path}")

# Get a common variable (PATH)
path_env = os.environ.get("PATH", "Not set")
print(f"PATH (first 50 chars): {path_env[:50]}...")

# --- Example 4: File operations (safe) ---
print("\n--- 4. File operations ---")
# Write a test file
with open("test_file.txt", "w") as f:
    f.write("Hello, world!")

# Check if it exists, get size
if os.path.exists("test_file.txt"):
    size = os.path.getsize("test_file.txt")
    print(f"test_file.txt exists, size: {size} bytes")
    # Clean up
    os.remove("test_file.txt")
    print("test_file.txt removed.")

# --- Example 5: Rename ---
print("\n--- 5. os.rename() ---")
with open("old_name.txt", "w") as f:
    f.write("Temporary file")
os.rename("old_name.txt", "new_name.txt")
print("Renamed old_name.txt to new_name.txt")
os.remove("new_name.txt")
print("Cleaned up.")


# =============================================================================
# PART 3: sys.argv – Command-Line Arguments
# =============================================================================

print("\n" + "-"*50)
print("PART 3: sys.argv – Command-Line Arguments")
print("-"*50)

print(f"\nScript name: {sys.argv[0]}")
print(f"Number of arguments: {len(sys.argv) - 1}")
print(f"Arguments: {sys.argv[1:]}")

# --- Example: Safe argument handling ---
print("\n--- Safe argument handling ---")
def get_filename_from_args():
    if len(sys.argv) < 2:
        print("Usage: python script.py <filename>")
        print("Using default: 'default.txt'")
        return "default.txt"
    return sys.argv[1]

filename = get_filename_from_args()
print(f"Using filename: {filename}")


# =============================================================================
# PART 4: sys.exit – Exiting the Program
# =============================================================================

print("\n" + "-"*50)
print("PART 4: sys.exit()")
print("-"*50)

print("\n--- sys.exit() demonstration ---")
print("(This example does not actually exit, it shows the pattern)")

# Example pattern (commented out so it doesn't exit):
# def check_file_exists(filename):
#     if not os.path.exists(filename):
#         print(f"Error: {filename} not found.")
#         sys.exit(1)
#     print(f"Found: {filename}")

print("""
Pattern:
    if not os.path.exists(filename):
        print(f"Error: {filename} not found.")
        sys.exit(1)
""")


# =============================================================================
# PART 5: sys.platform and sys.version
# =============================================================================

print("\n" + "-"*50)
print("PART 5: sys.platform and sys.version")
print("-"*50)

print(f"Platform: {sys.platform}")
print(f"Python version: {sys.version}")
print(f"Version info: {sys.version_info}")

# --- Detect OS ---
if sys.platform == "win32":
    print("Running on Windows")
elif sys.platform == "linux":
    print("Running on Linux")
elif sys.platform == "darwin":
    print("Running on macOS")
else:
    print(f"Unknown platform: {sys.platform}")


# =============================================================================
# COMMON MISTAKES
# =============================================================================

print("\n" + "-"*50)
print("COMMON MISTAKES TO AVOID")
print("-"*50)

print("""
❌ Mistake 1: Hardcoding paths with \\ or /
   path = "folder\\subfolder\\file.txt"  # Breaks on Linux/macOS
   Fix: path = os.path.join("folder", "subfolder", "file.txt")

❌ Mistake 2: Not checking if a file exists before opening
   with open("missing.txt", "r") as f:  # FileNotFoundError
   Fix: if os.path.exists("missing.txt"): ...

❌ Mistake 3: Using sys.argv[1] without checking length
   filename = sys.argv[1]  # IndexError if no argument
   Fix: if len(sys.argv) > 1: filename = sys.argv[1]

❌ Mistake 4: Using os.mkdir() when directory already exists
   os.mkdir("data")  # FileExistsError if data already exists
   Fix: os.makedirs("data", exist_ok=True)

❌ Mistake 5: Forgetting to import os or sys
   NameError
   Fix: import os, sys at the top.

❌ Mistake 6: Using sys.exit() without an error code
   sys.exit()  # Exits with 0 by default
   Fix: sys.exit(1) for errors, sys.exit(0) for success.
""")


# =============================================================================
# CORE EXERCISES (Mastery Check)
# =============================================================================

print("\n" + "="*70)
print("CORE EXERCISES (Mastery Check)")
print("="*70)

print("""
EXERCISE 1 (os.path):
Write a function get_file_size(filename) that:
1. Checks if the file exists.
2. If it does, returns the file size in bytes using os.path.getsize().
3. If it doesn't, returns None.

EXERCISE 2 (os Directory):
Write a function list_py_files(directory) that:
1. Lists all files in the given directory.
2. Returns only the files that end with .py.

EXERCISE 3 (sys.argv):
Write a program that:
1. Takes a filename as a command-line argument.
2. Prints the contents of the file.
3. If no argument is provided, prints "Usage: python my_script.py <filename>".
4. If the file doesn't exist, prints "File not found." and exits with error code 1.

EXERCISE 4 (Combined):
Write a program that:
1. Checks if library.json exists in the current directory.
2. If it exists, prints "Loading library..."
3. If it doesn't exist, prints "No library found. Creating a new one."
4. Then, regardless of whether it exists, creates a data/ folder (if it doesn't).
5. Uses sys to print the Python version you are using.
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

# 1. pathlib (Modern alternative)
print("\n--- 1. pathlib (Modern alternative) ---")
from pathlib import Path
path = Path("test_dir") / "file.txt"
print(f"pathlib path: {path}")

# 2. shutil (High-level file operations)
print("\n--- 2. shutil (High-level file operations) ---")
import shutil
# Copy a file
shutil.copy("handout_14_os_sys.py", "copy_of_handout.py")
print("Copied handout_14_os_sys.py to copy_of_handout.py")
os.remove("copy_of_handout.py")
print("Cleaned up.")

# 3. os.walk() (Recursive directory traversal)
print("\n--- 3. os.walk() (Recursive) ---")
print("Walking through current directory (first 5 items):")
count = 0
for root, dirs, files in os.walk("."):
    if count > 5:
        break
    print(f"  Root: {root}")
    count += 1

# 4. sys.stdin, sys.stdout, sys.stderr
print("\n--- 4. sys.stdin, sys.stdout, sys.stderr ---")
print("sys.stdin.read() reads from input (like input())")
print("sys.stdout.write() writes to output (like print())")
print("sys.stderr.write() writes to error stream")

# 5. sys.path
print("\n--- 5. sys.path (Module search path) ---")
print(f"Python looks for modules in: {sys.path[:3]}")

print("\n" + "="*70)
print("END OF HANDOUT #14")
print("="*70)