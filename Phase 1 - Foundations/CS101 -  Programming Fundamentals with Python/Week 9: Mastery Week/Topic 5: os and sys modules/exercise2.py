"""
Exercise 2 (os Directory):
Write a function list_py_files(directory) that:

- Lists all files in the given directory.
- Returns only the files that end with .py.
"""
import os

def list_py_files(directory: str):
    try:
        # if the directory does not exist.
        if not os.path.exists(directory):
            print(f"Directory: {directory} does not exist.")
            return None
    
    except ValueError:
        print(f"{directory} is not a valid directory. Provide a valid directory.")
        return None
    
    else:
        all_files = os.listdir(directory)

        py_files = [file for file in all_files if os.path.isfile(os.path.join(directory, file)) and file.endswith(".py")]
        
        return py_files
    
if __name__ == "__main__":
    print(list_py_files("sample"))

# Improved version using os:
import os

def list_py_files(directory: str):
    # Check if path exists AND is a directory
    if not os.path.exists(directory) or not os.path.isdir(directory):
        print(f"Error: '{directory}' is not a valid directory.")
        return []  # Return empty list instead of None
    
    try:
        all_files = os.listdir(directory)
        # Filter safely
        py_files = [
            file for file in all_files
            if os.path.isfile(os.path.join(directory, file)) and file.endswith(".py")
        ]
        return py_files
    except PermissionError:
        print(f"Error: Permission denied to access '{directory}'.")
        return []

if __name__ == "__main__":
    files = list_py_files("sample")
    if files:
        print(f"Found {len(files)} Python files:")
        for f in files:
            print(f" - {f}")
    else:
        print("No Python files found or invalid directory.")   

# Modern version (using pathlib)
# This is preferred approach in modern python:
from pathlib import Path

def list_py_files(directory: str):
    dir_path = Path(directory)
    
    # Check validity
    if not dir_path.exists() or not dir_path.is_dir():
        print(f"Error: '{directory}' is not a valid directory.")
        return []
    
    # Globbing is efficient and clean
    # rglob searches recursively, glob searches only top-level
    # We use glob() here to match your original logic (top-level only)
    try:
        return [p.name for p in dir_path.glob("*.py") if p.is_file()]
    except PermissionError:
        print(f"Error: Permission denied to access '{directory}'.")
        return []

if __name__ == "__main__":
    files = list_py_files("sample")
    print(f"Found: {files}")
