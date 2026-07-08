# EXTRACT DATES

import re

pattern = re.compile(r"\b(\d{4})-(\d{2})-(\d{2})\b")

text = """
Meeting:
2026-07-08
Birthday:
2001-04-11
"""

dates = pattern.findall(text)

for year, month, day in dates:
    print(f"Year: {year}, Month: {month}, Day: {day}")

for match in pattern.finditer(text):
    full_date = match.group(0) # The whole match: "2026-07-08"
    year = match.group(1)
    month = match.group(2)
    day = match.group(3)

print(f"Found {full_date} at position {match.start()}")   