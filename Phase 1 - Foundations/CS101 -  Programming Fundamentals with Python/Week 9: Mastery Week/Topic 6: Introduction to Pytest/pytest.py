#!/usr/bin/env python3
"""
================================================================================
HANDOUT #15: pytest (Mastery Week – Topic 6)
================================================================================
Student: ________________________________
Date: ___________________________________

This handout covers:
    1. What is unit testing?
    2. Installing pytest
    3. Writing test functions with assert
    4. Testing exceptions with pytest.raises
    5. The AAA pattern (Arrange, Act, Assert)
    6. Running pytest

This is a reference-only file. To run the tests, copy the examples into
separate files like test_basic.py and execute 'pytest' in the terminal.
================================================================================
"""

print("\n" + "="*70)
print("MASTERY WEEK – TOPIC 6: INTRODUCTION TO pytest")
print("="*70)

print("""
This topic is best learned by doing. Follow along with the examples below.

================================================================================
PART 1: What is Unit Testing?
================================================================================

A unit test verifies that a single unit of code (usually a function) works
correctly in isolation.

Characteristics of a good unit test:
    - Isolated: Tests one function only.
    - Repeatable: Same result every time.
    - Fast: Runs in milliseconds.
    - Self-Checking: Automatically passes or fails.

================================================================================
PART 2: Installing pytest
================================================================================

Make sure your virtual environment is active, then run:

    pip install pytest

Verify:
    pytest --version

================================================================================
PART 3: Writing a Test with assert
================================================================================

Example: test_basic.py

    def test_addition():
        assert 1 + 1 == 2
        assert 3 + 4 == 7

    def test_subtraction():
        assert 5 - 3 == 2

Run with:
    pytest

================================================================================
PART 4: Testing Functions
================================================================================

Function (calculator.py):
    def add(a, b):
        return a + b

    def divide(a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

Test (test_calculator.py):
    import pytest
    from calculator import add, divide

    def test_add():
        assert add(2, 3) == 5
        assert add(-1, 1) == 0

    def test_divide_by_zero():
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(10, 0)

================================================================================
PART 5: The AAA Pattern
================================================================================

Arrange - Set up the data.
Act     - Call the function.
Assert  - Verify the result.

Example:
    def test_search_books():
        # Arrange
        library = Library()
        library.add_book("1984", "Orwell")

        # Act
        results = library.search_by_author("Orwell")

        # Assert
        assert len(results) == 1
        assert results[0].title == "1984"

================================================================================
PART 6: Running pytest with Options
================================================================================

    pytest                # Run all tests
    pytest test_calc.py   # Run specific file
    pytest test_calc.py::test_add  # Run specific function
    pytest -v             # Verbose
    pytest -x             # Stop on first failure
    pytest -s             # Show print() output

================================================================================
PART 7: Core Exercises (Mastery Check)
================================================================================

EXERCISE 1 (Testing a Function):
Write a function is_palindrome(word) that returns True if the word is a
palindrome, and False otherwise. Then, write tests for:
    - "racecar" -> True
    - "hello" -> False
    - "" -> True (empty string)
    - "A" -> True (single character)

EXERCISE 2 (Testing with Edge Cases):
Write a function calculate_average(numbers) that returns the average of a list.
Write tests for:
    - [1, 2, 3] -> 2.0
    - [5, 10] -> 7.5
    - [] -> Should raise ValueError (empty list)
    - [0] -> 0.0

EXERCISE 3 (Testing a Class):
Define a Counter class with:
    - __init__(): initializes self.count = 0
    - increment(): adds 1
    - decrement(): subtracts 1
    - reset(): sets count to 0
    - get_count(): returns current count
Write tests for each method.

EXERCISE 4 (Integration with os and sys):
Write a function load_data(filename) that:
    - Opens and reads a JSON file.
    - Returns the loaded data.
    - Returns None if the file does not exist.
    - Raises ValueError if the file is corrupted.
Write tests for all three cases.
""")


# =============================================================================
# EXAMPLE CODE (To be copied into separate files)
# =============================================================================

print("\n" + "-"*50)
print("EXAMPLE CODE (Copy these into separate files to run)")
print("-"*50)

calculator_code = """
# calculator.py
def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
"""

test_calculator_code = """
# test_calculator.py
import pytest
from calculator import add, divide

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_divide():
    assert divide(10, 2) == 5
    assert divide(3, 2) == 1.5

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)
"""

print("\n--- calculator.py ---")
print(calculator_code)

print("\n--- test_calculator.py ---")
print(test_calculator_code)

print("""
================================================================================
HOW TO RUN:
1. Create a virtual environment: python -m venv venv
2. Activate it.
3. Install pytest: pip install pytest
4. Create calculator.py and test_calculator.py with the code above.
5. Run: pytest
================================================================================
""")


# =============================================================================
# ADVANCED EXTENSION (For Wandering)
# =============================================================================

print("\n" + "="*70)
print("ADVANCED EXTENSION (Optional - For Wandering)")
print("="*70)

print("""
The following concepts are EXTRA. They are NOT required for this topic.
Read them if you are curious.
""")

# 1. pytest.fixture (Reusable setup)
print("""
--- 1. pytest.fixture ---
Fixtures provide reusable test data.

    import pytest

    @pytest.fixture
    def library():
        lib = Library()
        lib.add_book("1984", "Orwell", 1949)
        return lib

    def test_search(library):
        results = library.search_by_author("Orwell")
        assert len(results) == 1
""")

# 2. pytest.mark.parametrize (Multiple inputs)
print("""
--- 2. pytest.mark.parametrize ---
Test multiple inputs with one function.

    import pytest

    @pytest.mark.parametrize("a, b, expected", [
        (2, 3, 5),
        (-1, 1, 0),
        (0, 0, 0),
    ])
    def test_add(a, b, expected):
        assert add(a, b) == expected
""")

# 3. Test-Driven Development (TDD)
print("""
--- 3. Test-Driven Development (TDD) ---
Write the test first, then write the code.

    Red:   Write a failing test.
    Green: Write the minimum code to pass the test.
    Refactor: Improve the code (tests ensure you don't break anything).
""")

# 4. pytest-cov (Code coverage)
print("""
--- 4. pytest-cov (Code Coverage) ---
Measures how much of your code is covered by tests.

    pip install pytest-cov
    pytest --cov=my_project --cov-report=term
""")

print("\n" + "="*70)
print("END OF HANDOUT #15")
print("="*70)