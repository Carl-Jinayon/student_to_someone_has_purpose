#!/usr/bin/env python3
"""
================================================================================
HANDOUT #9: OBJECT-ORIENTED PROGRAMMING (Step 9)
================================================================================
Student: ________________________________
Date: ___________________________________

This handout covers:
    1. Defining a class
    2. The __init__ method (constructor)
    3. Adding methods (behavior)
    4. Instance vs Class attributes
    5. __str__ and __repr__ (magic methods)
    6. Encapsulation (private attributes)
    7. Inheritance (super())
    8. The if __name__ == "__main__" guard

Prerequisites used: All previous steps.
================================================================================
"""

print("\n" + "="*70)
print("STEP 9: OBJECT-ORIENTED PROGRAMMING")
print("="*70)

# =============================================================================
# PART 1: Defining a Class with __init__
# =============================================================================

print("\n" + "-"*50)
print("PART 1: Basic Class and __init__")
print("-"*50)

class Dog:
    """A simple Dog class."""
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Creating objects (instances)
dog1 = Dog("Rex", 5)
dog2 = Dog("Bella", 3)

print(f"dog1: name={dog1.name}, age={dog1.age}")
print(f"dog2: name={dog2.name}, age={dog2.age}")


# =============================================================================
# PART 2: Adding Methods
# =============================================================================

print("\n" + "-"*50)
print("PART 2: Methods (Behavior)")
print("-"*50)

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says: Woof!")

    def get_human_age(self):
        """Dog years to human years (approx)."""
        return self.age * 7

    def __str__(self):
        return f"Dog(name={self.name}, age={self.age})"

dog = Dog("Rex", 5)
dog.bark()
human_age = dog.get_human_age()
print(f"Rex is {human_age} in human years.")
print(dog)   # Uses __str__


# =============================================================================
# PART 3: Instance vs Class Attributes
# =============================================================================

print("\n" + "-"*50)
print("PART 3: Instance vs Class Attributes")
print("-"*50)

class Dog:
    # Class attribute (shared by all dogs)
    species = "Canis familiaris"

    def __init__(self, name, age):
        # Instance attributes (specific to each dog)
        self.name = name
        self.age = age

dog1 = Dog("Rex", 5)
dog2 = Dog("Bella", 3)

print(f"dog1.species: {dog1.species}")   # Canis familiaris
print(f"dog2.species: {dog2.species}")   # Canis familiaris
print(f"Dog.species: {Dog.species}")     # Canis familiaris

# Changing a class attribute affects all instances
Dog.species = "Canis lupus familiaris"
print(f"After change: dog1.species = {dog1.species}")


# =============================================================================
# PART 4: __str__ and __repr__
# =============================================================================

print("\n" + "-"*50)
print("PART 4: __str__ and __repr__ (Magic Methods)")
print("-"*50)

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        """User-friendly string representation."""
        return f"Dog(name={self.name}, age={self.age})"

    def __repr__(self):
        """Developer-friendly string representation."""
        return f"Dog('{self.name}', {self.age})"

dog = Dog("Rex", 5)
print(f"print(dog): {dog}")          # Calls __str__
print(f"repr(dog): {repr(dog)}")     # Calls __repr__


# =============================================================================
# PART 5: Encapsulation (Private Attributes)
# =============================================================================

print("\n" + "-"*50)
print("PART 5: Encapsulation (Using _ for internal)")
print("-"*50)

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance   # Internal (by convention)

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            return True
        return False

    def get_balance(self):
        return self._balance

    def __str__(self):
        return f"Account(owner={self.owner}, balance={self._balance})"

account = BankAccount("Alice", 1000)
print(f"Initial: {account}")
account.deposit(500)
print(f"After deposit: {account}")
account.withdraw(200)
print(f"After withdraw: {account}")

# You can still access _balance, but you shouldn't.
# account._balance = 999999   # Works, but violates encapsulation.


# =============================================================================
# PART 6: Inheritance (super())
# =============================================================================

print("\n" + "-"*50)
print("PART 6: Inheritance and super()")
print("-"*50)

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        print(f"{self.name} makes a sound.")

    def __str__(self):
        return f"Animal(name={self.name}, species={self.species})"

class Dog(Animal):
    def __init__(self, name, breed):
        # Call the parent's __init__
        super().__init__(name, "Canine")
        self.breed = breed

    def speak(self):
        print(f"{self.name} says: Woof!")

    def __str__(self):
        return f"Dog(name={self.name}, breed={self.breed})"

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, "Feline")

    def speak(self):
        print(f"{self.name} says: Meow!")

# Usage
animals = [Dog("Rex", "Labrador"), Cat("Whiskers")]
for animal in animals:
    animal.speak()

print(Dog("Rex", "Labrador"))   # Uses Dog's __str__


# =============================================================================
# PART 7: The if __name__ == "__main__" Guard
# =============================================================================

print("\n" + "-"*50)
print("PART 7: The if __name__ == '__main__' Guard")
print("-"*50)

class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)

    def __str__(self):
        return f"Student: {self.name}, Average: {self.average():.1f}"

if __name__ == "__main__":
    # This code only runs when this file is executed directly.
    # It does NOT run if this file is imported by another script.
    student = Student("Alice", [85, 90, 78, 92])
    print(student)
    print("This file was run directly, not imported.")


# =============================================================================
# COMMON MISTAKES (Step 9 Edition)
# =============================================================================

print("\n" + "-"*50)
print("COMMON MISTAKES TO AVOID")
print("-"*50)

print("""
❌ Mistake 1: Forgetting 'self' in method parameters
   def bark():   # Missing self
       print("Woof!")
   # Fix: def bark(self):

❌ Mistake 2: Forgetting 'self' when accessing attributes
   def get_name(self):
       return name   # Should be self.name

❌ Mistake 3: Defining instance attributes outside __init__
   class Dog:
       def __init__(self, name):
           self.name = name
       def set_age(self, age):
           age = age   # This is a local variable, not self.age!
   # Fix: self.age = age

❌ Mistake 4: Typo in __init__ (single underscore or missing)
   class Dog:
       def _init_(self, name):  # Wrong
           self.name = name
   # Fix: def __init__(self, name):

❌ Mistake 5: Not calling super().__init__() in child class
   class Dog(Animal):
       def __init__(self, name):
           # Missing super().__init__(name, "Canine")
           self.name = name
   # Fix: call super().__init__(name, "Canine")

❌ Mistake 6: Using double __ for private attributes unnecessarily
   class Person:
       def __init__(self, name):
           self.__name = name  # Name mangling makes it hard to access
   # Fix: Use single _ for internal attributes.
""")


# =============================================================================
# CORE EXERCISES (Step 9 Mastery Check)
# =============================================================================

print("\n" + "="*70)
print("CORE EXERCISES (Step 9 Mastery Check)")
print("="*70)

print("""
EXERCISE 1 (Basic Class):
Define a class Book with:
- Attributes: title, author, year
- A method get_info() that returns "title by author (year)"
- A __str__ method that returns the same.

EXERCISE 2 (Encapsulation):
Define a class BankAccount with:
- Private attribute _balance (initial 0).
- Methods: deposit(amount), withdraw(amount), get_balance().
- deposit and withdraw should return True on success, False on failure.

EXERCISE 3 (Inheritance):
Define a base class Vehicle with:
- Attributes: make, model, year
- Method get_info() returns "make model (year)".

Define a subclass Car that inherits from Vehicle and adds:
- Attribute: num_doors
- Override get_info() to include doors: "make model (year) - 4 doors".

EXERCISE 4 (__str__ and Guard):
Create a class Student with name and grades (list).
- Method average() returns the average grade.
- __str__ returns "Student: name, Average: x.x".
- Use the if __name__ == "__main__": guard to create a student and print it.
""")


# =============================================================================
# 📌 ADVANCED EXTENSION (Optional - For Wandering)
# =============================================================================

print("\n" + "="*70)
print("ADVANCED EXTENSION (Optional - For Wandering)")
print("="*70)

print("""
The following concepts are EXTRA. They are NOT required for Step 9 mastery.
Read them if you are curious.
""")

# 1. @property (getters and setters)
print("\n--- 1. @property (Getters/Setters) ---")
class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value

p = Person("Alice", 30)
print(f"age: {p.age}")
p.age = 31
print(f"age after change: {p.age}")
# p.age = -5  # ValueError

# 2. __eq__ (equality)
print("\n--- 2. __eq__ (Equality) ---")
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y

p1 = Point(1, 2)
p2 = Point(1, 2)
p3 = Point(3, 4)
print(f"p1 == p2: {p1 == p2}")  # True
print(f"p1 == p3: {p1 == p3}")  # False

# 3. @classmethod and @staticmethod
print("\n--- 3. @classmethod and @staticmethod ---")
class School:
    name = "UP Diliman"

    def __init__(self, student_name):
        self.student_name = student_name

    @classmethod
    def change_school(cls, new_name):
        cls.name = new_name

    @staticmethod
    def is_valid_age(age):
        return age >= 5 and age <= 100

print(f"School name: {School.name}")
School.change_school("Ateneo")
print(f"School name after change: {School.name}")
print(f"Is 25 a valid age? {School.is_valid_age(25)}")

# 4. __slots__ (memory optimization)
print("\n--- 4. __slots__ (Memory Optimization) ---")
class Point2D:
    __slots__ = ("x", "y")
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point2D(1, 2)
print(f"Point2D: ({p.x}, {p.y})")
# p.z = 3  # AttributeError: 'Point2D' object has no attribute 'z'

# 5. Method Overriding (preview)
print("\n--- 5. Method Overriding ---")
class Parent:
    def greet(self):
        return "Hello from Parent"

class Child(Parent):
    def greet(self):
        return "Hello from Child"

obj = Child()
print(obj.greet())  # Hello from Child

print("\n" + "="*70)
print("END OF HANDOUT #9")
print("="*70)