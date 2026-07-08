import re

text = "aaa b aa"

print(re.findall(r"a*", text)) # '*' means 0 or more
print(re.findall(r"a+", text)) # '*' means 1 or more

text = "color colour"

print(re.findall(r"colou?r", text)) # one or zero

text = "+6398749238 +675489237 0987482974"
print(re.findall(r"(?:\+639)?\d+", text)) # without ?: it will only return what is inside the parenthesis. The '\d+' means one or more digits
print(re.findall(r"\d{4}", text)) # means four digits
text = "1 23 345 4567 43245"
print(re.findall(r"\d{2,4}", text)) # in between two numbers
print(re.findall(r"\d{4,}", text)) # means atleast the number