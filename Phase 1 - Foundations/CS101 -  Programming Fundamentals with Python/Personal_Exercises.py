# Type casting 

# Exercise 1: Write a function safe_divide(a, b) that:
# checks if a and b are numbers (int/float)
# Returns None if either is not a number
# Handles division by zero gracefully 
# Returns result as a float

def safe_divide(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return None
    
    if b <= 0:
        print("Divisor must not be zero.")
        return None
    
    return a / b

quotient = safe_divide(10, 3)
print(f"{quotient:.2f}")

# Exercise 2: 
"""
name of function - parse_user_input
Takes - value string, expected_type (int, float, bool, str)
returns the converted value
returns none if the conversion fails
"""

def parse_user_input(value: str, expected_type: str) -> any:
    
    if not isinstance(value, str) or not isinstance(expected_type, str):
        print("Invalid data type passed.")
        return None

    try:
        if expected_type != "int" and expected_type != "float" and expected_type != "bool" and expected_type != "str":
            print("Invalid type conversion")
            return None
        elif expected_type == "int":
            return int(value)
        elif expected_type == "float":
            return float(value)
        elif expected_type == "bool":
            return bool(value)
    except ValueError:
        return None

converted = parse_user_input("32", "int")
print(converted)

#--------------------------------------------------
# IMPROVED VERSION:
def parse_user_input(value: str, expected_type: str):
    """
    Parses a string value into the specified type using only standard Python.
    
    Args:
        value: The string to convert.
        expected_type: One of 'int', 'float', 'bool', 'str'.
        
    Returns:
        The converted value (int, float, bool, or str).
        
    Raises:
        ValueError: If conversion fails or type is unsupported.
        TypeError: If inputs are not strings.
    """
    # 1. Validate input types manually (since we aren't relying on a type checker)
    if not isinstance(value, str) or not isinstance(expected_type, str):
        raise TypeError("Both 'value' and 'expected_type' must be strings.")

    # 2. Define valid types and mapping
    valid_types = ("int", "float", "bool", "str")
    
    if expected_type not in valid_types:
        raise ValueError(f"Unsupported type '{expected_type}'. Must be one of {valid_types}.")

    # 3. Handle Boolean conversion explicitly (fixes the 'bool("false")' bug)
    if expected_type == "bool":
        normalized = value.strip().lower()
        if normalized in ("true", "1", "yes", "y", "t"):
            return True
        if normalized in ("false", "0", "no", "n", "f", ""):
            return False
        raise ValueError(f"Invalid boolean string: '{value}'")

    # 4. Use a dictionary for clean dispatching of other types
    converters = {
        "int": int,
        "float": float,
        "str": str  # Redundant but consistent
    }

    try:
        return converters[expected_type](value)
    except ValueError as e:
        # Re-raise with a clearer message if needed, or just let the original ValueError pass
        raise ValueError(f"Cannot convert '{value}' to {expected_type}: {e}")