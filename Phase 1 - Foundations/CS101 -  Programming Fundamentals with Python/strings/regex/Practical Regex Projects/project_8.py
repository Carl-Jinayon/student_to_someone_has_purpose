# PARSE LOG FILES

import re

line = "ERROR 2026-07-08 Connection failed"
pattern = r"(ERROR|INFO|WARNING)\s+(\d{4}-\d{2}-\d{2})\s+(.*)"
match = re.match(pattern, line)
print(match.groups())