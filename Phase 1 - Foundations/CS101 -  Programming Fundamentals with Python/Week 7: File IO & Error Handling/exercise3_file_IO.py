"""
Exercise 3 (Error Handling):
Write a function safe_divide(a, b) that:

Tries to divide a by b.
1. Returns the result if successful.
2. Handles ZeroDivisionError by printing "Cannot divide by zero" and returning None.
3. Handles TypeError (e.g., if a or b is not a number) by printing "Invalid type" and returning None.
"""

def safe_divide(a, b):

    try:
        return a / b
    except ZeroDivisionError:
        print("Cannot divide by zero.")
        return None
    except TypeError:
        print("Invalid type")
        return None

number = safe_divide(4234,0)
print(number)