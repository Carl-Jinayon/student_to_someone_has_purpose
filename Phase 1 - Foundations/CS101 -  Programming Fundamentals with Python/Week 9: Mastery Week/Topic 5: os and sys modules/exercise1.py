"""
Exercise 1 (os.path):
Write a function get_file_size(filename) that:

- Checks if the file exists.
- If it does, returns the file size in bytes using os.path.getsize().
- If it doesn't, returns None.
"""
import os

def get_file_size(filename: str):
    if not os.path.exists(filename):
        return None
    
    return os.path.getsize(filename)

if __name__ == "__main__":
    filename = "somewhere.txt"
    size_in_bytes = get_file_size(filename)

    if size_in_bytes is not None:
        print(f"The size of {filename}: {size_in_bytes:.2f}")
    else:
        print(f"The file '{filename}' does not exist.")

# Improved version:
import os

def get_file_size(filename: str):
    try:
        # Check existence and get size in one go inside try block
        # This handles race conditions where file is deleted between check and read
        if os.path.exists(filename) and os.path.isfile(filename):
            return os.path.getsize(filename)
        return None
    except (PermissionError, OSError):
        # Handles cases where file exists but is inaccessible
        return None

if __name__ == "__main__":
    filename = "somewhere.txt"
    size = get_file_size(filename)

    if size is not None:
        # Print as integer (no decimal places needed for bytes)
        print(f"The size of {filename}: {size} bytes")
    else:
        print(f"The file '{filename}' does not exist or is inaccessible.")   

# Pathlib version:
from pathlib import Path

def get_file_size(filename: str):
    file_path = Path(filename)
    
    try:
        # .stat() retrieves file metadata
        # .is_file() ensures it's not a directory
        if file_path.is_file():
            return file_path.stat().st_size
        return None
    except (PermissionError, OSError):
        return None

if __name__ == "__main__":
    filename = "somewhere.txt"
    size = get_file_size(filename)

    if size is not None:
        print(f"The size of {filename}: {size} bytes")
    else:
        print(f"The file '{filename}' does not exist or is inaccessible.")   