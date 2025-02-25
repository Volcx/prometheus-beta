import pytest
from src.string_converter import to_constant_case

def test_basic_string_conversion():
    """Test basic string to constant case conversion."""
    assert to_constant_case("hello world") == "HELLO_WORLD"
    assert to_constant_case("helloWorld") == "HELLO_WORLD"
    assert to_constant_case("HelloWorld") == "HELLO_WORLD"

def test_existing_constant_case():
    """Test that constant case strings remain unchanged."""
    assert to_constant_case("HELLO_WORLD") == "HELLO_WORLD"

def test_snake_case_conversion():
    """Test conversion from snake_case."""
    assert to_constant_case("hello_world") == "HELLO_WORLD"

def test_mixed_case_conversion():
    """Test conversion from mixed case strings."""
    assert to_constant_case("HelloWorld123Test") == "HELLO_WORLD_123_TEST"

def test_special_characters():
    """Test handling of special characters."""
    assert to_constant_case("hello-world!test") == "HELLO_WORLD_TEST"
    assert to_constant_case("hello world, test") == "HELLO_WORLD_TEST"

def test_empty_string():
    """Test handling of empty string."""
    assert to_constant_case("") == ""

def test_type_error():
    """Test that non-string inputs raise a TypeError."""
    with pytest.raises(TypeError):
        to_constant_case(123)
    
    with pytest.raises(TypeError):
        to_constant_case(None)

def test_unicode_characters():
    """Test handling of unicode characters."""
    assert to_constant_case("héllo wörld") == "HELLO_WORLD"