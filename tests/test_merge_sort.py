import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from merge_sort import merge_sort

def test_merge_sort_empty_list():
    """Test merge sort with an empty list."""
    assert merge_sort([]) == []

def test_merge_sort_single_element():
    """Test merge sort with a single-element list."""
    assert merge_sort([5]) == [5]

def test_merge_sort_sorted_list():
    """Test merge sort with an already sorted list."""
    input_list = [1, 2, 3, 4, 5]
    assert merge_sort(input_list) == input_list

def test_merge_sort_reverse_sorted_list():
    """Test merge sort with a reverse-sorted list."""
    input_list = [5, 4, 3, 2, 1]
    assert merge_sort(input_list) == [1, 2, 3, 4, 5]

def test_merge_sort_unsorted_list():
    """Test merge sort with an unsorted list."""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert merge_sort(input_list) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

def test_merge_sort_with_duplicates():
    """Test merge sort with a list containing duplicate elements."""
    input_list = [3, 3, 3, 1, 1, 4, 4]
    assert merge_sort(input_list) == [1, 1, 3, 3, 3, 4, 4]

def test_merge_sort_with_negative_numbers():
    """Test merge sort with a list containing negative numbers."""
    input_list = [-5, 3, -2, 0, 1, -10, 7]
    assert merge_sort(input_list) == [-10, -5, -2, 0, 1, 3, 7]

def test_merge_sort_with_floats():
    """Test merge sort with a list of floating-point numbers."""
    input_list = [3.14, 2.71, 1.41, 0.58]
    assert merge_sort(input_list) == [0.58, 1.41, 2.71, 3.14]

def test_merge_sort_input_type_error():
    """Test merge sort with an invalid input type."""
    with pytest.raises(TypeError, match="Input must be a list"):
        merge_sort("not a list")

def test_merge_sort_incomparable_elements():
    """Test merge sort with incomparable elements."""
    with pytest.raises(TypeError, match="List contains elements that cannot be compared"):
        merge_sort([1, 2, "3", 4])

def test_merge_sort_does_not_modify_original():
    """Test that merge sort does not modify the original list."""
    original_list = [3, 1, 4, 1, 5, 9, 2, 6]
    _ = merge_sort(original_list)
    assert original_list == [3, 1, 4, 1, 5, 9, 2, 6]