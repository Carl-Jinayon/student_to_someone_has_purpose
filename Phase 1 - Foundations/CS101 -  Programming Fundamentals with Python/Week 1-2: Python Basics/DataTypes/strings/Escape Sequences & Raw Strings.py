# Escape sequences:
# \n new line
# \t Tab
# \\ Backslash
# \" Double quote
# \' Single quote
# \b backspace
# \r carriage return

print("Hello fhsdk fsdkhjfsdk \rWorld sdfasdf  sdgds")

# Python as two ways to display a string.
# 1. using print()
# 2. using repr() - print(repr(text)) -> don't interpret the escape sequences

# Python can represent characteres by their unicode point.
print("\u2605")

# Encoding using UTF 8 converts Unicode to bytes
text = "😊"
data = text.encode("utf-8")
print(data)
data = data.decode("utf-8")
print(data)

# Mojibake - garbled text caused by using the wrong encoding.