import pytest
from src.longest_palindrome import longest_palindromic_substring

def test_basic_palindromes():
    """Test basic palindromic scenarios"""
    assert longest_palindromic_substring("babad") in ["bab", "aba"]
    assert longest_palindromic_substring("cbbd") == "bb"
    assert longest_palindromic_substring("a") == "a"

def test_edge_cases():
    """Test edge cases"""
    assert longest_palindromic_substring("") == ""
    assert longest_palindromic_substring(" ") == " "
    assert longest_palindromic_substring("  ") == "  "

def test_no_palindrome_longer_than_one():
    """Test strings with no palindrome longer than one character"""
    assert longest_palindromic_substring("abcd") in ["a", "b", "c", "d"]

def test_full_string_palindrome():
    """Test when entire string is a palindrome"""
    assert longest_palindromic_substring("racecar") == "racecar"
    assert longest_palindromic_substring("level") == "level"

def test_multiple_possible_palindromes():
    """Test scenarios with multiple possible palindromes"""
    assert longest_palindromic_substring("aacabdkacaa") in ["aca", "aa"]

def test_long_palindromes():
    """Test longer palindromic substrings"""
    assert longest_palindromic_substring("abaxyzzyxf") == "xyzzyx"

def test_unicode_support():
    """Test unicode character support"""
    result = longest_palindromic_substring("πορωπ")
    assert result == "πορωπ", f"Expected 'πορωπ', but got '{result}'"

def test_repeated_characters():
    """Test strings with repeated characters"""
    assert longest_palindromic_substring("aaaaaa") == "aaaaaa"
    assert longest_palindromic_substring("bbbbbb") == "bbbbbb"