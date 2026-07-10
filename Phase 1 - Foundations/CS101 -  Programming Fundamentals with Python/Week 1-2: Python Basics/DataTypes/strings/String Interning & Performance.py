# String interning - a process where multiple names are pointed into the same object

# When having a list object - don't think that interning might work

# Use interning manually:
import sys

a = sys.intern("Python")
b = sys.intern("Python")

print(a is b)