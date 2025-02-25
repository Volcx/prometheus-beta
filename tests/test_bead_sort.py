import pytest
from src.bead_sort import bead_sort

def test_basic_sorting():
    """Test basic sorting of positive integers."""
    assert bead_sort([5, 3, 1, 4, 2]) == [1, 2, 3, 4, 5]

def test_empty_list():
    """Test sorting an empty list."""
    assert bead_sort([]) == []

def test_single_element_list():
    """Test sorting a list with a single element."""
    assert bead_sort([42]) == [42]

def test_already_sorted_list():
    """Test sorting a list that is already sorted."""
    assert bead_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_reverse_sorted_list():
    """Test sorting a list in reverse order."""
    assert bead_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_list_with_duplicate_elements():
    """Test sorting a list with duplicate elements."""
    assert bead_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

def test_large_numbers():
    """Test sorting a list with larger numbers."""
    assert bead_sort([1000, 1, 100, 10]) == [1, 10, 100, 1000]

def test_invalid_input_negative_numbers():
    """Test that a ValueError is raised for negative numbers."""
    with pytest.raises(ValueError, match="All elements must be non-negative integers"):
        bead_sort([-1, 2, 3])

def test_invalid_input_non_integers():
    """Test that a TypeError is raised for non-integer inputs."""
    with pytest.raises(TypeError, match="Input must be a list"):
        bead_sort("not a list")
    
    with pytest.raises(ValueError, match="All elements must be non-negative integers"):
        bead_sort([1, 2, "3", 4])
        
def test_input_preservation():
    """Ensure the original input list is not modified."""
    original = [5, 3, 1, 4, 2]
    sorted_list = bead_sort(original)
    assert sorted_list == [1, 2, 3, 4, 5]
    assert original == [5, 3, 1, 4, 2]  # Original list unchanged