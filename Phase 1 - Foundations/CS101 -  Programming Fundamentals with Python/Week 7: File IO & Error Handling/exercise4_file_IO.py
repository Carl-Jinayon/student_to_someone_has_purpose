"""
Exercise 4 (File with Error Handling):
Write a program that:

1. Asks the user for a filename.
2. Tries to open and read the file.
3. If the file doesn't exist, prints "File not found" and creates an empty file with that name.
4. If the file exists, prints its content.
"""

filename = input("Enter filename: ")

try:
    with open(filename, "r", encoding="utf-8") as file:
        contents = file.read()
except FileNotFoundError:
    print("File does not found.")
    with open(filename, "w", encoding="utf-8") as file:
        pass
else:
    print("Reading file: Successful!")
finally:
    print("Program successfully terminated.")

print(contents)