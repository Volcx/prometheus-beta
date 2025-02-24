import pytest
from src.palindrome_counter import count_palindromic_substrings

def test_empty_string():
    """Test that an empty string returns 0 palindromic substrings."""
    assert count_palindromic_substrings("") == 0

def test_single_character():
    """Test that a single character is a palindrome."""
    assert count_palindromic_substrings("a") == 1

def test_two_characters_no_match():
    """Test two different characters."""
    assert count_palindromic_substrings("ab") == 2

def test_two_characters_match():
    """Test two matching characters."""
    assert count_palindromic_substrings("aa") == 3

def test_odd_length_palindromes():
    """Test a string with multiple odd-length palindromes."""
    assert count_palindromic_substrings("abc") == 3

def test_multiple_palindromes():
    """Test a string with multiple palindromic substrings."""
    assert count_palindromic_substrings("aaa") == 6

def test_mixed_palindromes():
    """Test a string with mixed palindromic substrings."""
    assert count_palindromic_substrings("abba") == 6

def test_longer_complex_string():
    """Test a longer string with multiple palindromes."""
    assert count_palindromic_substrings("racecar") == 10

def test_no_palindromes():
    """Test a string with no palindromes beyond single characters."""
    assert count_palindromic_substrings("abcd") == 4