# VALIDATE A PHILIPPINE MOBILE NUMBER

import re

pattern = r"^(09|\+639)\d{9}$"

numbers = [
    "09171234567",
    "08171234567",
    "09171234",
    "+639765724466"
]

for number in numbers:
    print(bool(re.fullmatch(pattern, number)))