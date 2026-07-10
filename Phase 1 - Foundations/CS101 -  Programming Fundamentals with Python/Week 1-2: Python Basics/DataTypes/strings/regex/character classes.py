import re

text = "apple banana cherry"
print(re.findall(r"[abc]", text))

# character ranges
text = "Python123"
print(re.findall(r"[a-z]", text)) # for lower case
print(re.findall(r"[A-Z]", text)) # for upper case
print(re.findall(r"[a-zA-z]", text)) # for lowercase and upper case
print(re.findall(r"[0-9]", text)) # for the digits
print(re.findall(r"[^0-9]", text)) # means get all except digits