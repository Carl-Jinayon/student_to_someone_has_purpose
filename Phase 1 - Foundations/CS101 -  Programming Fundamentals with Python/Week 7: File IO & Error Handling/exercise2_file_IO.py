"""
xercise 2 (JSON):
Write a program that:

1. Creates a list of dictionaries, where each dictionary represents a product ({"id": 1, "name": "Laptop", "price": 999.99}).
2. Writes this list to a JSON file called products.json.
3. Reads the JSON file and prints the total price of all products.
"""

import json

# product = {
#     "id": 1, "name": "Laptop", "price": 999.99
#     }

# Create a list to hold multiple product dictionaries
products = [
    {
        "id": 1, 
        "name": "Laptop", 
        "price": 999.99
    },
    {
        "id": 2, 
        "name": "Smartphone", 
        "price": 699.50
    },
    {
        "id": 3, 
        "name": "Headphones", 
        "price": 149.99
    }
]



total_price = 0
try:
    with open("products.json", "r", encoding="utf-8") as file:
        contents = json.load(file)
        
        # Calculate total price of all products
        for price in contents:
            total_price = total_price + price["price"]
except FileNotFoundError:
    print("File not found :<")
except Exception as e:
    print(f"Error: {e}")
else:
    print("Reading the json file is successful!")
finally:
    print("Program compeleted with no errors!")

print(f"Total price of products: {total_price}")
        
