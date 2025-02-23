import pytest
from src.longest_subsequence import longest_subsequence_with_target_sum

def test_basic_subsequence():
    """Test basic functionality with a simple array"""
    assert longest_subsequence_with_target_sum([1, 2, 3, 4, 5], 9) == 2

def test_multiple_subsequences():
    """Test when multiple subsequences can match the target"""
    assert longest_subsequence_with_target_sum([1, 1, 1, 1], 3) == 3

def test_empty_array():
    """Test with an empty array"""
    assert longest_subsequence_with_target_sum([], 5) == 0

def test_negative_target():
    """Test with a negative target"""
    assert longest_subsequence_with_target_sum([1, 2, 3], -1) == 0

def test_no_matching_subsequence():
    """Test when no subsequence matches the target"""
    assert longest_subsequence_with_target_sum([1, 2, 3], 10) == 0

def test_large_numbers():
    """Test with larger numbers"""
    assert longest_subsequence_with_target_sum([100, 200, 300, 400], 500) == 2

def test_zero_target():
    """Test with zero as target"""
    assert longest_subsequence_with_target_sum([0, 0, 1, 2], 0) == 2

def test_single_element_match():
    """Test when a single element matches the target"""
    assert longest_subsequence_with_target_sum([5, 2, 3], 5) == 1

def test_repeated_subsequence():
    """Test with repeated subsequences"""
    assert longest_subsequence_with_target_sum([2, 2, 2, 2, 2], 4) == 2