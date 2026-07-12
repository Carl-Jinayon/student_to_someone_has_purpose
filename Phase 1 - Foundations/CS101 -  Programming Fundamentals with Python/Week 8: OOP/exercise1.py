"""
Exercise 1 (Basic Class):
Define a class Book with:

1. Attributes: title, author, year
2. A method get_info() that returns "title by author (year)"
3. A __str__ method that returns the same.
"""

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    
    def get_info(self):
        return f"{self.title} by {self.author} ({self.year})"
    
    def __str__(self):
        return f"{self.title} by {self.author} ({self.year})"
    
my_book = Book("Undefined coincidence in nature.", "Jinayon, Carl", 2026)
print(my_book.get_info())
    