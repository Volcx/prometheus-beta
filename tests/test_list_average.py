import pytest
from src.list_average import calculate_average

def test_average_of_integers():
    """Test average calculation with integers."""
    assert calculate_average([1, 2, 3, 4, 5]) == 3.0

def test_average_of_floats():
    """Test average calculation with floating-point numbers."""
    assert calculate_average([1.5, 2.5, 3.5]) == 2.5

def test_average_with_single_element():
    """Test average calculation with a single element."""
    assert calculate_average([42]) == 42.0

def test_average_with_negative_numbers():
    """Test average calculation with negative numbers."""
    assert calculate_average([-1, 0, 1]) == 0.0

def test_empty_list_raises_error():
    """Test that an empty list raises a ValueError."""
    with pytest.raises(ValueError, match="Cannot calculate average of an empty list"):
        calculate_average([])

def test_non_list_input_raises_error():
    """Test that non-list input raises a TypeError."""
    with pytest.raises(TypeError, match="Input must be a list"):
        calculate_average("not a list")

def test_non_numeric_list_raises_error():
    """Test that a list with non-numeric elements raises a TypeError."""
    with pytest.raises(TypeError, match="All elements must be numeric"):
        calculate_average([1, 2, "three", 4])

def test_mixed_numeric_types():
    """Test average calculation with mixed numeric types."""
    assert calculate_average([1, 2.5, 3]) == 2.166666666666667