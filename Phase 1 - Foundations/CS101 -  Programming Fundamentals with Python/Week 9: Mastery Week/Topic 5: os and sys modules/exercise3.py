"""
Exercise 3 (sys.argv):
Write a program that:

Takes a filename as a command-line argument.

- Prints the contents of the file.
- If no argument is provided, prints "Usage: python my_script.py <filename>".
- If the file doesn't exist, prints "File not found." and exits with error code 1.
"""

import sys
import os
# Check if there is a argument or no.

def print_content():
    if len(sys.argv) < 2:
        print("Usage: python my_script.py <filename>")
        return 
    
    filename = sys.argv[1]

    if not os.path.exists(filename):
        print(f"File: {filename} not found.")
        sys.exit(1)

    if not os.path.isfile(filename):
        print(f"{filename} is not a file.")
        sys.exit(1)

    try:
        with open(filename, "r", encoding="utf-8") as file:
            contents = file.read()
            print(contents)
    except PermissionError:
        print(f"Error: Permission denied to read '{filename}")
        sys.exit(1)
    except UnicodeDecodeError:
        print(f"Error: Could not decode '{filename}' as UTF-8.")
        sys.exit(1)
    

print_content()

