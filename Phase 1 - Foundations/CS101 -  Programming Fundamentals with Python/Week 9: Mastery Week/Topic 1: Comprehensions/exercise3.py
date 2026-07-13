"""
Given a list of dictionaries:

Use a dict comprehension to create a new dictionary mapping "title" to "author".
"""

books = [{"title": "1984", "author": "Orwell"}, {"title": "Brave New World", "author": "Huxley"}]

title_author = {book.get("title"): book.get("author", "Unknown") for book in books}
print(title_author)