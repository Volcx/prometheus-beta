import pytest
from src.palindrome import is_palindrome

def test_classic_palindromes():
    """Test well-known palindrome phrases"""
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("race a car") == False

def test_simple_palindromes():
    """Test simple palindromes"""
    assert is_palindrome("radar") == True
    assert is_palindrome("hello") == False

def test_case_insensitivity():
    """Test that the function is case-insensitive"""
    assert is_palindrome("Able was I ere I saw Elba") == True

def test_empty_and_single_char():
    """Test empty string and single character"""
    assert is_palindrome("") == True
    assert is_palindrome("a") == True

def test_special_characters():
    """Test palindromes with various special characters"""
    assert is_palindrome("!@#$A man, a plan, a canal: Panama!@#$") == True
    assert is_palindrome("!@#$hello!@#$") == False

def test_numeric_palindromes():
    """Test numeric palindromes"""
    assert is_palindrome("123321") == True
    assert is_palindrome("12345") == False

def test_mixed_alphanumeric():
    """Test mixed alphanumeric palindromes"""
    assert is_palindrome("a1b2c33c2b1a") == True
    assert is_palindrome("a1b2c3") == False