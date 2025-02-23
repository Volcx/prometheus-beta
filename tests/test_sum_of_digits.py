import pytest
from src.sum_of_digits import sum_of_digits

def test_sum_of_digits_full_number():
    """Test with a full string of digits."""
    assert sum_of_digits('1234567890') == 45

def test_sum_of_digits_mixed_string():
    """Test with a mixed string containing digits."""
    assert sum_of_digits('abc123') == 6

def test_sum_of_digits_empty_string():
    """Test with an empty string."""
    assert sum_of_digits('') == 0

def test_sum_of_digits_no_digits():
    """Test with a string containing no digits."""
    assert sum_of_digits('hello') == 0

def test_sum_of_digits_leading_zeros():
    """Test that leading zeros are correctly handled."""
    assert sum_of_digits('00123') == 6

def test_sum_of_digits_scattered_zeros():
    """Test with scattered zeros in the string."""
    assert sum_of_digits('a0b1c0d2') == 3

def test_sum_of_digits_unicode_and_special_chars():
    """Test with unicode and special characters."""
    assert sum_of_digits('!@#$%^123&*()') == 6