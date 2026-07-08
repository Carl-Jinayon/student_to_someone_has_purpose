# The most important special sequences

# | Pattern | Meaning                                   |
# | ------- | ----------------------------------------- |
# | `\d`    | Digit                                     |
# | `\D`    | Not a digit                               |
# | `\w`    | Word character                            |
# | `\W`    | Not a word character                      |
# | `\s`    | Whitespace                                |
# | `\S`    | Not whitespace                            |
# | `.`     | Any character except newline (by default) | - any single character
# | `\b`    | Word boundary                             |
# | `\B`    | Not a word boundary                       |

# having a bracket and no bracket makes a huge difference:
# "."
# "[.]"

# \b - word boundary
# Example:
import re

text = "cat scatter category dog"
print(re.findall(r"\bcat\b", text)) # Outputs only the cat
print(re.findall(r"cat", text)) 
print(re.findall(r"[cat]", text)) 