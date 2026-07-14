from exercise1 import is_palindrome

def test_palindrome():
    assert is_palindrome("racecar") == True 
    assert is_palindrome("hello") == False 
    assert is_palindrome("") == True
    assert is_palindrome("A") == True  