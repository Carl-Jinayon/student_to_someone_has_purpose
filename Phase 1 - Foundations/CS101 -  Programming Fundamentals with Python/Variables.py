"""
age = 19
age is just a name, 19 is the object.

How assignment really works?
1. create an integer object (which is the 19)
2. Create the name age.
3. Bind the name to the object.

Naming rules:
1. Must begin with underscore or letter (cannot begin in number).
2. May contain letters, digits, underscores (hyphens are interpreted as subtraction).
3. No spaces.
4. Cannot use python keywords

Naming Conventions (PEP 8)
Good:
student_name
total_score
is_logged_in
learning_rate
Bad:
x1
abc
temp123
A
myvariable

Python uses snake_case.

Multiple Assignment:
x,y,z = 10, 20, 30
Equivalent to:
x = 10
y = 20
z = 30
This is called tuple unpacking.

Assigning the same value:
a = b = c 100
This is generally safe for immutable objects like integers.

Swapping Variables:
a, b = b, a

Python doesn't have true constants.
Instead, developers use UPPER_CASE to signal that a value shouldn't be changed.
PI = 3.14159
MAX_USERS = 100
SECONDS_PER_DAY = 86400
"""