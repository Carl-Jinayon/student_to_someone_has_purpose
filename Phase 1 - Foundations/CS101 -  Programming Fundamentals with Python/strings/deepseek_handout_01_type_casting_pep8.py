#!/usr/bin/env python3
"""
================================================================================
HANDOUT #1: TYPE CASTING, TYPE CHECKING & PEP 8
================================================================================
Student: ________________________________
Date: ___________________________________

This handout is your complete reference for:
    1. Type Checking (isinstance, type)
    2. Type Casting / Conversion (int, float, str, bool, list, etc.)
    3. Python's Style Guide (PEP 8) – the rules and the tools

Run this file to execute demonstration examples.
================================================================================
"""

# =============================================================================
# PART 1: TYPE CHECKING – KNOWING WHAT YOU HAVE
# =============================================================================

"""
WHY TYPE CHECKING MATTERS:
--------------------------
Python is dynamically typed. A variable can hold an integer at one moment and a
string the next. Type checking prevents runtime crashes by verifying data
before you operate on it.

REAL-WORLD USE CASES:
---------------------
- API responses: ensure fields are the expected type before using them.
- User input: validate form data (age must be int, email must be str).
- File parsing: confirm data types before mathematical operations.
- Machine Learning: ensure model inputs are float32, not strings.

THE TOOLS:
----------
1. type()            -> Returns the exact class of the object.
                      -> Does NOT respect inheritance.
                      -> Example: type(True) is bool, but bool is a subclass of int.

2. isinstance()      -> Checks if an object is an instance of a given class or tuple.
                      -> RESPECTS inheritance. This is the PREFERRED method.
                      -> Example: isinstance(True, int) returns True.

3. issubclass()      -> Checks if a class is a subclass of another.
"""

def demo_type_checking():
    """Demonstrate type() vs isinstance() vs issubclass()"""
    print("\n" + "="*70)
    print("DEMO: Type Checking")
    print("="*70)

    values = [5, 3.14, "hello", True, None, [1, 2, 3], {"a": 1}]

    for v in values:
        print(f"Value: {repr(v):<15} | type() = {type(v).__name__:<12} | isinstance(v, int)? {isinstance(v, int)}")

    # CRITICAL: bool is a subclass of int
    print("\nCRITICAL INSIGHT: bool is a subclass of int")
    print(f"  type(True) == int? {type(True) == int}")           # False
    print(f"  isinstance(True, int)? {isinstance(True, int)}")   # True  <-- USE THIS

    # issubclass() example
    print(f"\n  issubclass(bool, int)? {issubclass(bool, int)}") # True


# =============================================================================
# PART 2: TYPE CASTING / CONVERSION – CHANGING WHAT YOU HAVE
# =============================================================================

"""
WHY TYPE CASTING MATTERS:
-------------------------
Data rarely arrives in the format you need. Forms send strings. APIs send JSON
(strings). Files send bytes. You MUST convert them to usable types.

THE CASTING FUNCTIONS:
----------------------
1. int(x)      -> Converts to integer. Truncates floats. Strips whitespace from strings.
                -> Raises ValueError if string contains non-numeric characters.

2. float(x)    -> Converts to float. Handles strings with decimals.

3. str(x)      -> Converts to string. Works on anything.

4. bool(x)     -> Converts to boolean.
                -> FALSY values: 0, 0.0, "", [], {}, set(), None.
                -> TRUTHY values: everything else.
                -> WARNING: bool("False") is True (non-empty string).

5. list(x)     -> Converts iterable to list. (e.g., list("abc") -> ['a', 'b', 'c'])
6. tuple(x)    -> Converts iterable to tuple.
7. set(x)      -> Converts iterable to set (removes duplicates).
8. dict(x)     -> Converts sequence of key-value pairs to dict.

IMPLICIT CASTING (COERCION):
----------------------------
Python automatically converts in some cases:
    int + float -> float
    int + bool -> int (True=1, False=0)
    str + str -> str
    BUT: str + int -> TypeError (Python won't guess)
"""

def demo_type_casting():
    """Demonstrate all casting functions and common pitfalls."""
    print("\n" + "="*70)
    print("DEMO: Type Casting")
    print("="*70)

    # Basic conversions
    print("--- BASIC CONVERSIONS ---")
    print(f"int('5'):        {int('5')}          (type: {type(int('5')).__name__})")
    print(f"int('  5  '):    {int('  5  ')}      (strips whitespace)")
    print(f"int(3.9):        {int(3.9)}          (TRUNCATES, does NOT round)")
    print(f"float('3.14'):   {float('3.14')}     (type: {type(float('3.14')).__name__})")
    print(f"str(5):          {repr(str(5))}      (type: {type(str(5)).__name__})")
    print(f"bool(0):         {bool(0)}           (Falsy)")
    print(f"bool([]):        {bool([])}          (Falsy)")
    print(f"bool('hello'):   {bool('hello')}     (Truthy)")
    print(f"bool('False'):   {bool('False')}     (TRUTHY! Non-empty string)")

    # Collection conversions
    print("\n--- COLLECTION CONVERSIONS ---")
    print(f"list('abc'):           {list('abc')}")
    print(f"tuple([1, 2, 3]):      {tuple([1, 2, 3])}")
    print(f"set([1, 2, 2, 3]):     {set([1, 2, 2, 3])}")

    # CRITICAL: String to integer with decimal
    print("\n--- CRITICAL PITFALL ---")
    try:
        int("5.0")
    except ValueError as e:
        print(f"❌ int('5.0') raises: {e}")
    print("✅ Fix: int(float('5.0')) ->", int(float("5.0")))


# =============================================================================
# PART 3: SAFE CASTING PATTERN (PRODUCTION-GRADE)
# =============================================================================

"""
THE PRODUCTION PATTERN:
-----------------------
Never cast blindly. Always:
    1. Check the type (or attempt the cast safely).
    2. Handle conversion failures gracefully.
    3. Validate the value after casting.

GOLDEN RULE: External input is NEVER trusted.
             - User input
             - API responses
             - File contents
             - Database queries
             -> All of these MUST be validated and cast.
"""

def safe_int(value, default=None):
    """
    Safely convert any value to int.
    Returns default (or None) if conversion fails.
    """
    try:
        # If it's a string, strip whitespace first.
        if isinstance(value, str):
            value = value.strip()
        # Convert to float first to handle "5.0" strings, then to int.
        # This handles "5.0" gracefully.
        if isinstance(value, (int, float)):
            return int(value)
        # Handle boolean explicitly: True->1, False->0
        if isinstance(value, bool):
            return int(value)
        # For strings: try float -> int
        if isinstance(value, str):
            return int(float(value))
        return int(value)
    except (ValueError, TypeError):
        return default

def demo_safe_casting():
    """Demonstrate the production-safe casting pattern."""
    print("\n" + "="*70)
    print("DEMO: Safe Casting Pattern")
    print("="*70)

    test_values = ["5", "5.0", "  3.14  ", "abc", None, True, False, 42, 3.9]

    for v in test_values:
        result = safe_int(v, default=-999)
        print(f"safe_int({repr(v)}) -> {result} (type: {type(result).__name__ if result is not None else 'None'})")


# =============================================================================
# PART 4: PEP 8 – THE PYTHON STYLE GUIDE
# =============================================================================

"""
WHAT IS PEP 8?
--------------
PEP 8 is Python's official style guide. It defines how code should be formatted
to ensure consistency across the entire Python community.

WHY IT MATTERS:
---------------
- Code is read FAR more often than it is written.
- Consistency reduces cognitive load.
- Open source projects REQUIRE PEP 8 compliance.
- Code reviews should focus on LOGIC, not formatting.

CORE RULES:
-----------
1. INDENTATION:
   - Use 4 spaces per level. NEVER use tabs.
   - Continuation lines should align with opening delimiter or use hanging indent.

2. LINE LENGTH:
   - Maximum 79 characters for code.
   - Maximum 72 characters for docstrings/comments.
   (Modern teams sometimes use 88-100, but learn the standard first.)

3. BLANK LINES:
   - 2 blank lines between top-level functions and classes.
   - 1 blank line between methods in a class.
   - Use blank lines sparingly inside functions to separate logical sections.

4. IMPORTS:
   - Each import on its own line.
   - Group imports in this order:
        1. Standard library (os, sys, math, ...)
        2. Third-party libraries (numpy, pandas, ...)
        3. Local application modules.
   - NEVER use `from module import *` (pollutes namespace).

5. NAMING CONVENTIONS:
   - Variables, functions, methods -> snake_case (e.g., user_name, calculate_total)
   - Classes -> PascalCase (e.g., CustomerOrder)
   - Constants -> UPPER_SNAKE_CASE (e.g., MAX_RETRIES)
   - Internal/private -> _leading_underscore (e.g., _internal_state)
   - Magic/dunder -> __double_underscore__ (e.g., __init__)

6. WHITESPACE:
   - Space around operators: `x = 5`, `a + b`
   - Space after commas: `function(arg1, arg2, arg3)`
   - NO space before parentheses: `function()` not `function ()`
   - In function signatures, NO spaces around = for defaults:
        `def func(param1, param2=default)`  # correct
        `def func(param1, param2 = default)` # incorrect

7. DOCSTRINGS:
   - Use `\"""triple double quotes\"""`.
   - Modules, classes, and public functions MUST have docstrings.
   - Google style or NumPy style are widely used.

8. STRING QUOTES:
   - Pick either `'` or `"` and stick to it.
   - Use `'` for strings, and `"` for strings containing single quotes.
     (Or vice versa, as long as it's consistent.)

AUTOMATION TOOLS (USE THESE RELIGIOUSLY):
-----------------------------------------
- black        -> Auto-formatter. Opinionated. No configuration needed.
- ruff         -> Ultra-fast linter (replaces flake8, pylint, isort).
- isort        -> Sorts imports alphabetically.

VS CODE SETUP:
--------------
{
    "python.formatting.provider": "black",
    "editor.formatOnSave": true,
    "python.linting.enabled": true,
    "python.linting.ruffEnabled": true
}

PRE-COMMIT HOOK (Industry Standard):
------------------------------------
Add this to .pre-commit-config.yaml:
    - repo: https://github.com/psf/black
      rev: 23.3.0
      hooks:
        - id: black
    - repo: https://github.com/astral-sh/ruff-pre-commit
      rev: v0.1.0
      hooks:
        - id: ruff
""" 

# =============================================================================
# PEP 8 DEMONSTRATION (A WELL-FORMATTED EXAMPLE)
# =============================================================================

"""
This section shows a properly formatted Python module following PEP 8 rules.
Compare this to the poorly formatted version in the exercise.
"""

# Imports: Standard library first, one per line.
import json
import math
import sys
from datetime import datetime

# Imports: Third-party next.
# import numpy as np  # (commented for this demo)
# import pandas as pd

# Constants: UPPER_SNAKE_CASE.
MAX_RETRIES = 3
DEFAULT_TIMEOUT = 30.0


class DatabaseConnection:
    """
    Manages a connection to the database.

    This class handles connection pooling, reconnection logic, and query
    execution. All methods are thread-safe.

    Attributes:
        host: Database host address.
        port: Database port (default 5432).
        _connection: Internal connection object (private).
    """

    def __init__(self, host: str, port: int = 5432):
        self.host = host
        self.port = port
        self._connection = None

    def connect(self) -> bool:
        """
        Establish a connection to the database.

        Returns:
            True if connection succeeded, False otherwise.

        Raises:
            ConnectionError: If the database is unreachable.
        """
        # Simulate connection logic.
        self._connection = f"Connected to {self.host}:{self.port}"
        return True

    def _reconnect(self) -> None:
        """
        Internal method to re-establish connection.

        This is called automatically when a query fails due to network issues.
        Not part of the public API.
        """
        self._connection = f"Reconnected to {self.host}:{self.port}"


def calculate_total(price: float, tax_rate: float) -> float:
    """
    Calculate the total price including tax.

    Args:
        price: Base price of the item.
        tax_rate: Tax rate as a decimal (e.g., 0.12 for 12%).

    Returns:
        Total price including tax.

    Example:
        >>> calculate_total(100.0, 0.12)
        112.0
    """
    return price * (1 + tax_rate)


# =============================================================================
# COMMON MISTAKES – QUICK REFERENCE TABLE
# =============================================================================

"""
| MISTAKE                           | WHY IT'S WRONG                               | FIX                                        |
|-----------------------------------|----------------------------------------------|--------------------------------------------|
| int("5.0")                        | ValueError: decimal string to int            | int(float("5.0"))                          |
| type(value) == int                | Fails for bool (subclass)                    | isinstance(value, int)                     |
| Casting without try/except        | Silent failures or crashes                   | Wrap in try/except                         |
| bool("False")                     | True (non-empty string)                      | s.lower() == "true"                        |
| Not checking None                 | AttributeError on None                       | if value is not None:                      |
| Using tabs for indentation        | Python 3 rejects mixed tabs/spaces           | Set editor to use spaces (4)               |
| Mixing tabs and spaces            | Inconsistent appearance                      | Use black to auto-fix                      |
| Importing with *                  | Pollutes namespace, hard to trace            | Import explicitly: from math import sqrt   |
| Ignoring PEP 8                    | Bad habits; rejected PRs                     | Use black + ruff from day one              |
| Long lines > 79 chars             | Hard to read side-by-side                    | Break with parentheses                     |
"""


# =============================================================================
# CHEAT SHEET – QUICK REFERENCE
# =============================================================================

"""
TYPE CHECKING CHEAT SHEET:
--------------------------
isinstance(value, int)                      -> True if int or bool
isinstance(value, str)                      -> True if str
isinstance(value, (int, float))             -> True if either
isinstance(value, collections.abc.Iterable) -> True if iterable

TYPE CASTING CHEAT SHEET:
-------------------------
int("5")          -> 5
float("3.14")     -> 3.14
str(5)            -> "5"
bool(0)           -> False
bool([])          -> False
bool("")          -> False
list("abc")       -> ['a', 'b', 'c']
tuple([1, 2])     -> (1, 2)
set([1, 2, 2])    -> {1, 2}

SAFE CASTING PATTERN:
---------------------
try:
    result = int(raw_value)
except (ValueError, TypeError):
    result = default_value

PEP 8 NAMING CHEAT SHEET:
-------------------------
Variables/Functions/Methods  -> snake_case        -> user_name, calculate_total
Classes                      -> PascalCase        -> CustomerOrder
Constants                    -> UPPER_SNAKE_CASE  -> MAX_RETRIES
Private/Internal             -> _leading_underscore -> _internal_state
Magic/Dunder                 -> __double_underscore__ -> __init__
"""


# =============================================================================
# MAIN EXECUTION – RUN ALL DEMOS
# =============================================================================

if __name__ == "__main__":
    print("\n" + "="*70)
    print("          HANDOUT #1: DEMONSTRATION EXECUTION")
    print("="*70)
    print("This file serves as your complete reference handout.")
    print("Study the code, run the demos, and keep this file as your guide.")
    print("="*70)

    demo_type_checking()
    demo_type_casting()
    demo_safe_casting()

    print("\n" + "="*70)
    print("END OF DEMONSTRATION")
    print("="*70)
    print("\n📌 NEXT STEPS:")
    print("  1. Save this file as 'handout_01_type_casting_pep8.py'")
    print("  2. Run it: python handout_01_type_casting_pep8.py")
    print("  3. Use it as your reference for all type-related questions.")
    print("  4. Configure VS Code with black + ruff (see PEP 8 section).")
    print("  5. Refactor your previous projects to follow PEP 8.")