# Numbers with a fractional part
# Approximate value (for many decimals)
# Fixed precision (typically 64-bit IEEE 754 in CPython)

# Floats are also objects.

# Very large or very small numbers are commonly written using exponent notation.

# Integer to float conversion and Float to Integer Conversion
print(float(10))
int(10.00) # it truncaates not round.
print(2.5 * 4)
print(5.1 + 1.2 == 6.3)
print(3e2)
x = 0.3
print(type(x))

'''
actually produces something very close to 0.3, but not exactly equal due to how floating-point numbers are represented in binary.
We'll spend an entire lesson explaining why. It requires understanding the IEEE 754 floating-point standard, 
and it's one of the most famous topics in Computer Science.
'''

# Comparing FLoats:

# never write: 
# if x == y:

# instead:
import math

x = None
y = None

math.isclose(x, y)

# When not to use float? adding floats
# Instead use decimal module:
from decimal import Decimal

price = Decimal("0.1") + Decimal("0.2")
print(price)




