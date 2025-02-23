import pytest
from src.list_sum_calculator import calculate_sum

def test_calculate_sum_normal_case():
    """Test sum calculation with a typical list of integers."""
    test_list = [1, 2, 3, 4, 5]
    assert calculate_sum(test_list) == 40  # 0*1 + 1*2 + 2*3 + 3*4 + 4*5 = 40

def test_calculate_sum_empty_list():
    """Test calculation with an empty list."""
    assert calculate_sum([]) == 0

def test_calculate_sum_single_element():
    """Test calculation with a single-element list."""
    assert calculate_sum([10]) == 0

def test_calculate_sum_negative_numbers():
    """Test calculation with negative numbers."""
    test_list = [-1, -2, -3, -4, -5]
    assert calculate_sum(test_list) == -40

def test_calculate_sum_mixed_numbers():
    """Test calculation with mixed positive and negative numbers."""
    test_list = [-1, 2, -3, 4, -5]
    assert calculate_sum(test_list) == -12  # Corrected expected result

def test_calculate_sum_non_list_input():
    """Test that a TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        calculate_sum(123)
        calculate_sum("not a list")
        calculate_sum(None)

def test_calculate_sum_non_integer_elements():
    """Test that a TypeError is raised for non-integer list elements."""
    with pytest.raises(TypeError, match="All elements must be integers"):
        calculate_sum([1, 2, '3', 4, 5])
        calculate_sum([1.5, 2, 3])
        calculate_sum([1, None, 3])