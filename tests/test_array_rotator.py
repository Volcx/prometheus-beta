import pytest
from src.array_rotator import rotate_array_left

def test_basic_rotation():
    """Test basic left rotation of an array."""
    assert rotate_array_left([1, 2, 3, 4, 5], 2) == [3, 4, 5, 1, 2]

def test_full_rotation():
    """Test rotation equal to array length (no change)."""
    assert rotate_array_left([1, 2, 3, 4, 5], 5) == [1, 2, 3, 4, 5]

def test_rotation_larger_than_length():
    """Test rotation amount larger than array length."""
    assert rotate_array_left([1, 2, 3, 4, 5], 7) == [3, 4, 5, 1, 2]

def test_empty_array():
    """Test rotation of an empty array."""
    assert rotate_array_left([], 3) == []

def test_single_element_array():
    """Test rotation of a single-element array."""
    assert rotate_array_left([42], 1) == [42]

def test_invalid_input_type():
    """Test error handling for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        rotate_array_left("not a list", 2)

def test_invalid_rotation_type():
    """Test error handling for non-integer rotation amount."""
    with pytest.raises(TypeError, match="Rotation amount must be an integer"):
        rotate_array_left([1, 2, 3], "2")

def test_negative_rotation():
    """Test error handling for negative rotation amount."""
    with pytest.raises(ValueError, match="Rotation amount cannot be negative"):
        rotate_array_left([1, 2, 3], -1)

def test_zero_rotation():
    """Test rotation of 0 positions."""
    assert rotate_array_left([1, 2, 3, 4, 5], 0) == [1, 2, 3, 4, 5]