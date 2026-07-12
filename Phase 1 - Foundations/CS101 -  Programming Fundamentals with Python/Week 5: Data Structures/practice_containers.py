person = {
    "name" : "Alice", 
    "age" : 30, 
    "city" : "Manila"
}

person.get("city", "Cavite")
print(person.get("city"))

for key in person:
    print(key, person[key])

s = {1,2,3}

for value in s:
    print(value, end=" ")

tups = 30,40

# Create list:
listt = [2, "two", False, 32.23] 
print(f"\n{listt}")

# Modify a list:
listt[2] = "True"
print(listt)

# Insert at the end using append
listt.append("appended")
print(listt)

# Insert using insert function:
listt.insert(0, "inserted using insert function")
print(listt)

# Remove the last element:
listt.pop()
print(listt)

# Remove items using remove function:
listt.remove("inserted using insert function")
print(listt)

# Creation of Tuple:
tuplee = (2, "two", False, 32.23, 32.23)
print("two" in tuplee)

# Common set operations:
# | union - all elements from both
# & intersection - common elements
# - - in a but not in b
# ^ symmetric difference - in either, but not both