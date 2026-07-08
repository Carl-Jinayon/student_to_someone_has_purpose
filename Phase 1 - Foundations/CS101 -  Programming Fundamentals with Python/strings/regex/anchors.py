# To validate the start of the string, the pattern must have '^'

# To validate the end of the string, the pattern must have '$'

# So for example you are validating a string that:
# Start with 2 capital letters, and ends with 4 digit numbers
# Then the regex pattern must be:
    # ^[A-Z]{2}\d{4}$

# The difference between [0-9] - for ASCII only
# \d is for UNICODE
import re

text = "CS2021"

print(re.search(r"^[A-Z]{2}\d{4}$", text).group())

pattern = re.compile(r"\d{3}-\d{3}-\d{4}")
valid = pattern.search("Call 123-456-7890")   
print(valid.group())