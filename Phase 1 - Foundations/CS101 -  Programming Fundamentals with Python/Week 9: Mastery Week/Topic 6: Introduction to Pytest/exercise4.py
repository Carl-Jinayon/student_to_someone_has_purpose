"""
Exercise 4 (Integration with os and sys):

Write a function load_data(filename) that:
- Tries to open and read a JSON file.
- Returns the loaded data if successful.
- Returns None if the file does not exist.
- Raises ValueError if the file is corrupted (invalid JSON).

Then, write tests that:
- Create a temporary JSON file, load it, and verify it works.
- Attempt to load a non-existent file, and verify it returns None.
- Attempt to load a corrupted file, and verify it raises ValueError.
"""
import json

def load_data(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
            print("File loaded sucessfully.")
            return data
    
    except FileNotFoundError:
        print(f"File: '{filename}' does not exist.")
        return None
    
    except json.JSONDecodeError as e:
        raise ValueError(f"Error: The file '{filename}' contains invalid JSON (corrupted).")

    except UnicodeDecodeError:
        print(f"Error: The file '{filename}' is not valid UTF-8 text.")

