import os
import pytest
from src.file_search import search_string_in_file

def test_search_string_exists():
    # Create a temporary test file
    with open('tests/test_file.txt', 'w') as f:
        f.write("Hello world\nThis is a test file\nWith multiple lines\nHello again")
    
    # Search for existing string
    result = search_string_in_file('tests/test_file.txt', 'Hello')
    assert result == [1, 4], "Should find 'Hello' on lines 1 and 4"
    
    # Clean up test file
    os.remove('tests/test_file.txt')

def test_search_string_not_exists():
    # Create a temporary test file
    with open('tests/test_file.txt', 'w') as f:
        f.write("Hello world\nThis is a test file")
    
    # Search for non-existing string
    result = search_string_in_file('tests/test_file.txt', 'Python')
    assert result == [], "Should return empty list when string not found"
    
    # Clean up test file
    os.remove('tests/test_file.txt')

def test_search_empty_string():
    # Create a temporary test file
    with open('tests/test_file.txt', 'w') as f:
        f.write("Hello world\nThis is a test file")
    
    # Search for empty string
    result = search_string_in_file('tests/test_file.txt', '')
    assert result == [1, 2], "Empty string should match all lines"
    
    # Clean up test file
    os.remove('tests/test_file.txt')

def test_file_not_found():
    # Test file not found error
    with pytest.raises(FileNotFoundError):
        search_string_in_file('nonexistent_file.txt', 'test')

def test_invalid_input_types():
    # Test invalid input types
    with pytest.raises(TypeError):
        search_string_in_file(123, 'test')
    
    with pytest.raises(TypeError):
        search_string_in_file('file.txt', 123)