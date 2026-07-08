# VALIDATE USERNAME

# Rules:
# 1. 5-20 characters
# 2. has letters
# 3. has numbers
# 4. has underscore
# 5. must start with a letter

# import re

# username = input("Enter username: ") # ex: the username entered is "123carl"

# pattern = re.compile(r"^([A-Za-z]\w){5,20}$") - wrong because one group can contain 2 characters.
# pattern = re.compile(r"^[A-Za-z]\w{4,19}$") # true answer.
# print(bool(pattern.match(username)))

import re

pattern = re.compile(r"^[A-Za-z]\w{4,19}$")

usernames = [
    "Carl123", 
    "123carl", 
    "john_doe",
    "ab"
]

for username in usernames:
    if pattern.fullmatch(username):
        print(f"{username} : Valid")
    else:
        print(f"{username} : Invalid")