import re

# 1. re.search(pattern, string, flags=0)
# Description: Scans the entire string to find the first location where the regex pattern produces a match.
# Use Case: Checking if a pattern exists anywhere in a string or retrieving details of the first occurrence.
match = re.search(r"\d+", "Order #1234")
if match:
    print(f"re.search result: {match.group()}")  # Output: 1234

# 2. re.match(pattern, string, flags=0)
# Description: Checks for a match only at the beginning of the string.
# Use Case: Validating input formats where the pattern must start at the first character.
match_start = re.match(r"[A-Z]", "Hello")  # Matches
match_fail = re.match(r"[A-Z]", " hello")  # Returns None
print(f"re.match result: {match_start.group() if match_start else None}")

# 3. re.findall(pattern, string, flags=0)
# Description: Returns a list of all non-overlapping matches of the pattern in the string.
# Use Case: Extracting all occurrences of a pattern (e.g., all emails, numbers, or words).
nums = re.findall(r"\d+", "IDs: 10, 20, 30")
print(f"re.findall result: {nums}")  # Output: ['10', '20', '30']

# 4. re.sub(pattern, repl, string, count=0, flags=0)
# Description: Finds all occurrences of the pattern and replaces them with 'repl'.
# Use Case: Cleaning text, redacting sensitive data, or formatting strings.
cleaned = re.sub(r"\s+", " ", "Too   many   spaces")
print(f"re.sub result: {cleaned}")  # Output: "Too many spaces"

# 5. re.split(pattern, string, maxsplit=0, flags=0)
# Description: Splits the string by the occurrences of the pattern, returning a list of substrings.
# Use Case: Tokenizing text with complex or inconsistent delimiters.
parts = re.split(r"[,;\s]+", "apple,orange;banana grape")
print(f"re.split result: {parts}")  # Output: ['apple', 'orange', 'banana', 'grape']

# 6. re.compile(pattern, flags=0)
# Description: Compiles a regex pattern into a pattern object for reuse.
# Use Case: Improving performance and readability when the same pattern is used multiple times.
pattern = re.compile(r"\d{3}-\d{3}-\d{4}")
valid = pattern.search("Call 123-456-7890")
print(f"re.compile result: {valid.group() if valid else None}")

# 7. re.fullmatch(pattern, string, flags=0)
# Description: Returns a match object only if the entire string matches the pattern.
# Use Case: Strict validation where the whole input must conform to the pattern.
match_full = re.fullmatch(r"\d{4}", "2024")  # Matches
match_fail_full = re.fullmatch(r"\d{4}", "20245")  # Returns None
print(f"re.fullmatch result: {match_full.group() if match_full else None}")   