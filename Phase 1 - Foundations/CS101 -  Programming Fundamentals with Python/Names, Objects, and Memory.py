"""
Pillar 1: Object is a piece of data that exists in memory.

Every object has three important properties
1. Identity - id() function
2. Type - type() function
3. Value - value is the value of a variable

+------------------------+
| Type : int             |
| Value: 10              |
| ID   : 12345           |
+------------------------+

Second Pillar: Names
1. Create an integer objet
+------------------------+
| Type : int             |
| Value: 10              |
| ID   : 12345           |
+------------------------+
2. Create the name
x
3. Bind the name to the object
x
│
▼
+--------------------+
| int                |
| value = 10         |
+--------------------+

Pillar 3: References

A reference is simply the connection between a name and an object.
student_name
      │
      ▼
" Carl "
Think of it as an arrow.
Name
 │
 ▼
Object

Multiple Names Can Reference One Object
a = [1, 2]

b = a
a
│
│
└──────┐
       ▼
    +---------+
    | [1, 2]  |
    +---------+
       ▲
┌──────┘
│
b
"""