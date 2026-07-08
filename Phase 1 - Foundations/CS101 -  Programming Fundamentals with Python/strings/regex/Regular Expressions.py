# Regex functionality lives in Python's buiilt-in re module.
import re

text = "Python is awesome"
result = re.search("Python", text)
print(result)
print(result.group()) # retrived the first matched text
print(result.start()) # retrived the index of the start of the string
print(result.end())  # retrived the index after the end of the matched string

text = "cat dog car bird cat"
matches = re.findall("cat", text)
print(matches) # returns all the matching word using list

# Sometimes you need more information:
for match in re.finditer("cat", text):
    print(match.start(), match.group())
    
# Raw Strings and Regex
# instead of "\\d"
# Professionals write: r\"d"

# Regex is case sensitive by default;
print(re.search("python", "Python", re.IGNORECASE)) # use ignore case
