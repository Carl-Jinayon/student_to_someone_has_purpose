# groupings are the use of parenthesis

import re

text = "CS2026"

match = re.search(r"([A-Z]{2})(\d{4})", text)

print(match.group()) # retrives the entire match
print(match.group(1)) # retrives the first group
print(match.group(2)) # retrives the second group

# instead of retriving one group at a time use:
print(match.groups()) 

# you can have nested groups
# print(match.group())
# Group 1 - abc
# Group 2 - ab

# We can name groups:
pattern = (
    r"(?P<year>\d{4})-"
    r"(?P<month>\d{2})-"
    r"(?P<day>\d{2})"
)
match = re.search(pattern, "2026-07-08")
print(match.group("year"))

# Access all named groups:
print(match.groupdict())
# {
#     'year': '2026',
#     'month': '07',
#     'day': '08'
# }

# Capturing vs Non-Cpaturing Groups
# instead of (ab) use (?:ab)

# Example:
match = re.search(r"(?:ab)+", "ababab")
print(match.group())
# There will be no group 1 because the group was not captured.