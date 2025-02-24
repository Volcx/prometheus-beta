import pytest
from src.array_processor import process_multidim_array

def test_basic_processing():
    """Test basic multi-dimensional array processing"""
    input_array = [[1, 2, 3], [4, 5], [6, 7, 8]]
    expected = [8, 7, 6, 5, 4, 3, 2, 1]
    assert process_multidim_array(input_array) == expected

def test_empty_subarrays():
    """Test removal of empty sub-arrays"""
    input_array = [[1, 2], [], [3, 4], []]
    expected = [4, 3, 2, 1]
    assert process_multidim_array(input_array) == expected

def test_duplicate_removal():
    """Test duplicate removal while maintaining order"""
    input_array = [[1, 2, 2], [3, 1, 4], [4, 5]]
    expected = [5, 4, 3, 2, 1]
    assert process_multidim_array(input_array) == expected

def test_mixed_type_array():
    """Test array with mixed types"""
    input_array = [[1, 'a'], ['b', 2], [3, 'a']]
    expected = ['a', 2, 'b', 3, 1]
    assert process_multidim_array(input_array) == expected

def test_nested_subarrays():
    """Test nested subarrays (should treat as flat)"""
    input_array = [[1, [2, 3]], [4, [5, 6]]]
    expected = [6, 5, 4, 3, 2, 1]
    assert process_multidim_array(input_array) == expected

def test_invalid_input():
    """Test invalid input type"""
    with pytest.raises(TypeError):
        process_multidim_array("not a list")

def test_empty_input():
    """Test empty input list"""
    assert process_multidim_array([]) == []