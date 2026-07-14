"""
Exercise 1 (Testing a Function):

Write a function is_palindrome(word) that returns True if the word is a palindrome (reads the same backward), and False otherwise. 
Then, write tests for:

- "racecar" → True
- "hello" → False
- "" → True (empty string)
- "A" → True (single character)
"""

def is_palindrome(word):
    print(word[::-2])
    return True if word == word[::-1] else False

is_palindrome("racecar")