"""
Exercise 4 (Combined):
Write a program that:

Checks if library.json exists in the current directory.

- If it exists, prints "Loading library..."
- If it doesn't exist, prints "No library found. Creating a new one."
- Then, regardless of whether it exists, creates a data/ folder (if it doesn't exist).
- Uses sys` to print the Python version you are using.
"""
import os
import sys

def library():
    filename = "library.json"

    if os.path.exists(filename):
        print("Loading library...")
        with open(filename, "r", encoding="utf-8") as file:
            contents = file.read()
            print(contents)
    else:
        print("No library found. Creating a new one.")
        with open(filename, "w", encoding="utf-8") as file:
            file.write("Write JSON here.")   

    os.makedirs("data/", exist_ok=True)

    print(f"Python version: {sys.version}")

library()
