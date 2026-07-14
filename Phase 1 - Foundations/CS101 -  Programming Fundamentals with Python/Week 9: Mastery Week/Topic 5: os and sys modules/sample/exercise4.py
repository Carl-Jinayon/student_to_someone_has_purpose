"""
Exercise 4 (Combined enumerate + zip):
Given two lists:

products = ["Laptop", "Mouse", "Keyboard"]
prices = [999.99, 25.50, 75.00]

Use enumerate and zip together to print a numbered list of products with prices, formatted as:
1. Laptop - $999.99
2. Mouse - $25.50
3. Keyboard - $75.00
"""

products = ["Laptop", "Mouse", "Keyboard"]
prices = [999.99, 25.50, 75.00]

for i, (product, price) in enumerate(zip(products, prices), start=1):
    print(f"{i}. {product} - ${price:.2f}")