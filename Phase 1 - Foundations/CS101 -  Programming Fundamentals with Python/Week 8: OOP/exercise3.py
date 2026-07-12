"""
Exercise 3 (Inheritance):
Define a base class Vehicle with:
1. Attributes: make, model, year
2. Method get_info() returns "make model (year)".
Define a subclass Car that inherits from Vehicle and adds:
1. Attribute: num_doors
2. Override get_info() to include doors: "make model (year) - 4 doors".
"""

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def get_info(self):
        return f"{self.make} {self.model} ({self.year})"
    
    def __str__(self):
        return self.get_info()    
    
class Car(Vehicle):
    def __init__(self, make, model, year, doors):
        super().__init__(make, model, year)
        
        if not (all(isinstance(x, str) for x in [make, model, year]) and isinstance(doors, int)):
            raise ValueError("Make, model, and year must be in string types.")
        self.doors = doors
    
    def get_info(self):
        return f"{self.make} {self.model} ({self.year}) - {self.doors} doors."
    
    def __str__(self):
        return self.get_info()

my_car = Car("POCO", "f4", "2019", "4")
print(my_car)
