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
    # Use pytest.raises to test for exceptions
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)