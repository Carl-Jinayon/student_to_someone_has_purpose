print(isinstance("5", int)) # Checks if the parameter corresponds to the given data type

issubclass(bool, int) # bool is a subclass of int since they represents 0 and 1

# Booleans are only true or false, you can convet 0 and 1s using 
bool(0)
bool(1)

bool([]) # false
bool([1]) # true

# Booleans are immutable

# truthiness and falsiness

something = "something"

if something: # should thisobject behave as True or False?
    print(something) # If an object constains meaningful data, it is usually truthy.

# if an object is empty or the data type is none, it is identified as false.

names = []

if names:
    print("has names")
else: 
    print("no names stored.")

# Professionals use

password = " "

# if not password: instead of if password == ""

if not password:
    print("is empty")
else:
    print("has letters")