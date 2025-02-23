import pytest
from src.string_utils import remove_char_length

def test_remove_char_length_basic():
    """Test basic functionality of removing a character and getting length."""
    assert remove_char_length("hello", "l") == 3
    assert remove_char_length("python", "p") == 5
    assert remove_char_length("aabbaa", "a") == 2

def test_remove_char_length_no_occurrence():
    """Test when the character does not exist in the string."""
    assert remove_char_length("hello", "x") == 5

def test_remove_char_length_empty_string():
    """Test with an empty string."""
    assert remove_char_length("", "a") == 0

def test_remove_char_length_all_chars_removed():
    """Test when all characters are removed."""
    assert remove_char_length("aaaaa", "a") == 0

def test_remove_char_length_invalid_inputs():
    """Test error handling for invalid inputs."""
    # Test non-string inputs
    with pytest.raises(TypeError, match="Input must be a string"):
        remove_char_length(123, "a")
    
    with pytest.raises(TypeError, match="Character to remove must be a string"):
        remove_char_length("hello", 1)
    
    # Test multi-character input
    with pytest.raises(ValueError, match="Character to remove must be a single character"):
        remove_char_length("hello", "ab")

def test_remove_char_length_case_sensitive():
    """Test case sensitivity of character removal."""
    assert remove_char_length("Hello", "h") == 5
    assert remove_char_length("Hello", "H") == 4