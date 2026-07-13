"""
Exercise 4 (Combining):
Given a list of strings ["Hello", "World", "Python", "is", "Fun"], use map and filter together (or comprehensions) to:

1. Filter out words shorter than 3 characters.
2. Convert the remaining words to uppercase.
3. Print the result as a list.
"""

my_list = ["Hello", "World", "Python", "is", "Fun"]

print(list(map(lambda word: word.upper(), filter(lambda word: len(word) >= 3, my_list))))
