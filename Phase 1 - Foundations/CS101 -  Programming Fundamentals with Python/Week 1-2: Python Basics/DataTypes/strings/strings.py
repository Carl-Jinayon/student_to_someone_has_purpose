# Strings are objects

# Create strings using single quotes and double quotes
# Triple quotes for multi-line comments


# Empt strings contain zero characters.
empty = ""
print(len(empty))

# Indexing
word = "Python"
print(word[0]) # prints 'w'
# Negative Indexing
print(word[-1]) # prints the last letter 'n'

# 'Index Error' if the indices printed is invalid..

# Strings are immutable - cannot be changed
word = "Jython"
print(word)

print(len(word)) # string length

# Space counts as characters

# Escape characters:
greetings = "He said \"Hello\""

# Common escape sequences:

# Escape	Meaning
# \n	New line
# \t	Tab
# \\	Backslash
# \"	Double quote
# \'	Single quote

# Python supports unicode