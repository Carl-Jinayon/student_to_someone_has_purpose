# TYPECASTING

# Functions
#type() # Returns the data type.
#isinstance() # expects two parameters and returns boolean

# You cannnot typecase directly from float to integer
int(float(5.0)) # You can use this method

# TYPE CONVERSION
# - if the parameter has empty value, then it is false.

# IMPLICIT CASTING
True + 5 # Boolean values are converted to correspoding value.

x = 4

if x is not None:
    print("X is not none.")

# Summary:
# verify the variable first using isinstance()
# verify using type() - this is rarely used
# just choose between isinstance and type
# explicit casting
# Safe casting - try/except + isinstance()
# Type Hints

# Industry perspective:
# use of pydantic for automatic data validation, error handling, type safety, easy integration
# To install: pip install pydantic

# Example usage:
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
    email: str

# valid data
user = User(name="Alice", age = 25, email = "alice25@gamil.com")
print(user)

# invalid data
try:
    invalid_user = User(name = "Bob", age = "thirty", email = "bob30@gmail.com")
except ValueError as e:
    print(e)


# Mypy
# Type annotation for warning - like assigning variable a datatype
# numbers: int = 4342

# To install mypy: pip3 install mypy
# i just did install an extension in vscode named "mypy type checker"