"""
- Create a temporary JSON file, load it, and verify it works.
- Attempt to load a non-existent file, and verify it returns None.
- Attempt to load a corrupted file, and verify it raises ValueError.
"""
import pytest
import json
from pathlib import Path

from exercise4 import load_data

TEST_DIR = Path(__file__).parent

def test_load_data():
    test_file = TEST_DIR / "valid_temp.json"

    with open(test_file, "r", encoding="utf-8") as file:
        result = json.load(file)

    from_function = load_data(test_file)
    
    assert from_function == result
    
def test_nonexistent():
    test_file = TEST_DIR / "test.json"

    assert load_data(test_file) == None

def test_corrupted():
    test_file = TEST_DIR / "corrupted.json"
    
    with pytest.raises(ValueError):
        load_data(test_file)   
