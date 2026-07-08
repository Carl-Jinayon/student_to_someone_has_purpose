# EXTRACT EMAIL ADDRESS

import re 

EMAIL_REGEX = re.compile(
    r"\b(?![.])"              # Cannot start with a dot
    r"(?!.*[.]{2})"          # Cannot have consecutive dots
    r"[a-zA-Z0-9._%+-]+"     # Local part (includes . _ % + -)
    r"@"
    r"[a-zA-Z0-9.-]+"        # Domain name
    r"\.[a-zA-Z]{2,}\b"       # TLD (min 2 chars)
)

text = """
alice@example.com
bob@test.org
"""

print(EMAIL_REGEX.findall(text))