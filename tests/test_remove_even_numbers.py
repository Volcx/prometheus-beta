import pytest
from src.remove_even_numbers import remove_even_numbers_and_sum

def test_remove_even_numbers_basic():
    """Test basic functionality of removing and summing even numbers."""
    nums = [1, 2, 3, 4, 5, 6]
    result = remove_even_numbers_and_sum(nums)
    assert result == 12  # Sum of 2, 4, 6
    assert nums == [1, 3, 5]  # Remaining list should be odd numbers

def test_remove_even_numbers_no_evens():
    """Test case where no even numbers are present."""
    nums = [1, 3, 5, 7]
    result = remove_even_numbers_and_sum(nums)
    assert result == 0
    assert nums == [1, 3, 5, 7]

def test_remove_even_numbers_all_evens():
    """Test case where all numbers are even."""
    nums = [2, 4, 6, 8]
    result = remove_even_numbers_and_sum(nums)
    assert result == 20
    assert nums == []

def test_remove_even_numbers_empty_list():
    """Test case with an empty list."""
    nums = []
    result = remove_even_numbers_and_sum(nums)
    assert result == 0
    assert nums == []

def test_invalid_input_not_list():
    """Test that TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        remove_even_numbers_and_sum("not a list")

def test_invalid_input_non_integers():
    """Test that TypeError is raised for non-integer elements."""
    with pytest.raises(TypeError, match="All elements must be integers"):
        remove_even_numbers_and_sum([1, 2, 3, "four"])