"""
Exercise 1 (Write and Read):
Write a program that:

1. Asks the user for their name and age.
2. Writes this data to a file called user_data.txt in the format: Name: Alice, Age: 30.
3. Reads the file back and prints the content.
"""

name = input("Enter your name: ")
age = int(input("Enter your age: "))

with open("user_data.txt", "a", encoding="utf-8") as file:
    file.write(f"Name: {name}, Age: {age}")

try:
    with open("user_data.txt", "r", encoding="utf-8") as file:
        contents = file.read()
        print(contents)
except Exception as e:
    print(f"Somethings went wrong: {e}")
except FileNotFoundError:
    print("Error! File not found.")
else:
    print("Reading the data was successful!")
finally:
    print("Operation completed.")

