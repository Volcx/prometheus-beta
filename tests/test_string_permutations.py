import pytest
from src.string_permutations import generate_unique_permutations

def test_empty_string():
    """Test empty string input."""
    assert generate_unique_permutations('') == []

def test_single_character():
    """Test single character input."""
    assert generate_unique_permutations('a') == ['a']

def test_unique_characters():
    """Test string with unique characters."""
    result = generate_unique_permutations('abc')
    expected = ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    assert sorted(result) == sorted(expected)

def test_repeated_characters():
    """Test string with repeated characters."""
    result = generate_unique_permutations('aba')
    expected = ['aab', 'aba', 'baa']
    assert sorted(result) == sorted(expected)

def test_multiple_repeated_characters():
    """Test string with multiple repeated characters."""
    result = generate_unique_permutations('aabb')
    expected = ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
    assert sorted(result) == sorted(expected)

def test_invalid_input():
    """Test invalid input types."""
    with pytest.raises(TypeError):
        generate_unique_permutations(123)
    
    with pytest.raises(TypeError):
        generate_unique_permutations(None)

def test_complex_repeated_pattern():
    """Test a complex string with repeated characters."""
    result = generate_unique_permutations('aabbc')
    assert len(result) == 60  # Mathematically correct number of unique permutations