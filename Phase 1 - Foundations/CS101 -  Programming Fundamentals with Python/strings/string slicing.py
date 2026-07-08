# Slice Syntax:
# string[start:stop] - stop is not included

# Concatenation:
word = "Python"

first = word[:3]
second = word[3:]

print(first + second)

# Not specifying means going from the end or up to the end.

# Step parameter:
# word[start:stop:step]
step = word[::2]
print(step)

# When you try to use negative 1 (-1) as a step is serves as reversing the string
