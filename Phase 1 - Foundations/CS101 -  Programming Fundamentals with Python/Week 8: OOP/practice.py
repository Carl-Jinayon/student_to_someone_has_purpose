class Dog:
    # Class attr
    breed = "Canis familiaris"

    """A simple Dog class"""
    # Instance attr
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says: woof!")

    def get_human_age(self):
        """Dog years converted to human years (approx)."""
        return self.age * 7

# Creating Object
dog1 = Dog("Rudolf", 4)
dog2 = Dog("Mark", 6)

print("First Dog:")
print(f"Name: {dog1.name}, Age: {dog1.age}")
print("Second Dog: ")
print(f"Name: {dog2.name}, Age: {dog2.age}",)

print(f"First dog age converted to human time: {dog1.get_human_age()}")
print(repr("jkfhskaf\n"))