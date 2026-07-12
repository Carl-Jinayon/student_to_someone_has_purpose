"""
Exercise 1 (List):
Write a function average_list(numbers) that takes
 a list of numbers and returns their average. 
Test it with [10, 20, 30, 40].
"""

def average_list(numbers: list):
    return sum(numbers) / len(numbers)

print(average_list([10, 20, 30, 40]))

# To improve add zerodivisionerror
def average_list(numbers: list[int | float]) -> float:
    if not numbers:  # Handles empty lists safely
        return 0.0
    return sum(numbers) / len(numbers)

# Test cases
print(average_list([10, 20, 30, 40]))  # Output: 25.0
print(average_list([]))                # Output: 0.0 (No error)   


"""
Exercise 2 (Tuple):
Write a function min_max_tuple(data)
that takes a list of numbers and
returns a tuple (min, max). 
Test it with [5, 2, 8, 1, 9].
"""

def min_max_tuple(data: list[int | float]) -> tuple[int, int] | None:
    if not data:
        return None
    return (min(data), max(data))

print(min_max_tuple([5, 2, 8, 1, 9]))

# but since you have to return a tuple you can do
# return (None, None) - then change the hints

"""
Exercise 3 (Dict):
Write a function char_count(text) 
that takes a string and returns a 
dictionary with the count of each character. 
Test it with "hello" 
(should return {'h':1, 'e':1, 'l':2, 'o':1}).
"""

def char_count(text: str) -> dict:
    chars = dict()
    for character in text:
        if character not in chars:
            chars[character] = 1
        else:
            chars[character] += 1
    return chars

# You can use chars.get(characters, 0) - 0 is the default value
# if the key hasn't been yet existed.
# So it will be:
# chars[character] = chars.get(character, 0) + 1

print(char_count("hello"))

from collections import Counter

def char_count2(text: str) -> dict:
    return dict(Counter(text))

# Or simply return Counter(text) if a dict subclass is acceptable   
print (char_count2("hello"))

"""
Exercise 4 (Set):
Write a function common_elements(list1, list2) 
that returns a set of elements common to both lists. 
Test it with [1,2,3,4] and [3,4,5,6] (should return {3,4}).
"""

def common_elements(list1: set, list2: set) -> set:
    return list1 & list2

print(common_elements({1,2,3,4}, {3,4,5,6}))

"""
Exercise 5 (Combining):
Write a function unique_values(data) 
that takes a list and returns a list of 
unique values, keeping the order of first appearance. 
(Hint: use a set to track seen values, 
but the final result should be a list that preserves order.)
"""

def unique_values(data: list) -> list:
    empty_set = set()
    empty_list = list()

    for item in data:
        if item not in empty_set:
            empty_set.add(item)
            empty_list.append(item)
    return empty_list

print(unique_values(["apple", "banana", "apple", "orange", "banana", "Apple"]))

# Improved: 
def unique_values(data: list) -> list:
    """
    How it works: dict.fromkeys(data) creates
    a dictionary where keys are the list items 
    (automatically removing duplicates) and values are None. 
    Converting keys back to a list preserves the order.
    """
    return list(dict.fromkeys(data))   
