text = "Hello"

new_text = text.upper() # Creates a new object "HELLO"

# Category 1: Changing letter case
# upper()
# lower()
# tilte() - This capitalizes first letter of every word
# capitalize() - This capitalizes only the first letter of the first word.
# swapcase() - Uppercase becomes lowercase and vice versa
# 
# Category 2: Removing Whitespaces
# strip() - removes whitespace from both ends.
# lstrip() - removes only whitespaces from the left.
# rstrip() - removes only whitespaces from the right.
# 
# Category 3: Searching
# find("") - returns the index of the first letter of the searched word. If not found it returns negative one (-1)
# index("") - similar but differs if the word does not exist, it returns ValueError
#
# Category 4: Replacing
# replace("existing word", "new word")
# 
# Category 5: Splitting
# split(you can place parameter here on how you will split the string) - returns a list of strings
# Example:
sentence = "Python is awesome"
language, pointer, adjective = sentence.split()
print(language, pointer, adjective) 
# 
# Category 6: Joining - opposite of split
# "string_that_is_in_between_ of_words".join(words)
#
# Category 7: Checking
# startswith("")
# endswith("")
# isalpha() - checks if the string is only letters
# isdigit() - checks if the string is only digits
# isalnum() - checks if the string is letters and digits only
# isspace() - checks if the string is only whitespaces

# Knowledge check:
# Write a single line of code that checks whether "resume.pdf" ends with the .pdf extension.
name = "   Carl   "
name = name.strip().lower()
print(name)