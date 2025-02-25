import pytest
from src.alternating_caps import to_alternating_caps

def test_basic_alternating_caps():
    """Test basic string conversion to alternating caps."""
    assert to_alternating_caps("hello") == "HeLlO"
    assert to_alternating_caps("world") == "WoRlD"

def test_empty_string():
    """Test handling of empty string."""
    assert to_alternating_caps("") == ""

def test_single_character():
    """Test single character conversion."""
    assert to_alternating_caps("a") == "A"
    assert to_alternating_caps("B") == "B"

def test_string_with_spaces():
    """Test string with spaces."""
    assert to_alternating_caps("hello world") == "HeLlO WoRlD"

def test_string_with_numbers_and_symbols():
    """Test string with mixed characters."""
    assert to_alternating_caps("hello123 world!") == "HeLlO123 WoRlD!"

def test_invalid_input_type():
    """Test error handling for non-string inputs."""
    with pytest.raises(TypeError, match="Input must be a string"):
        to_alternating_caps(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        to_alternating_caps(None)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        to_alternating_caps(["hello"])