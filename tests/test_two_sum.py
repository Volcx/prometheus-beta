import pytest
from src.two_sum import two_sum

def test_two_sum_with_matching_pair():
    """Test that function returns True when a pair summing to target exists"""
    assert two_sum([1, 2, 3, 4], 7) == True
    assert two_sum([10, 15, 3, 7], 17) == True

def test_two_sum_without_matching_pair():
    """Test that function returns False when no pair sums to target"""
    assert two_sum([1, 2, 3, 4], 10) == False
    assert two_sum([5, 6, 7, 8], 3) == False

def test_two_sum_edge_cases():
    """Test edge cases like empty list, single element, zero target"""
    assert two_sum([], 5) == False
    assert two_sum([5], 10) == False
    assert two_sum([0, 0], 0) == False

def test_two_sum_negative_numbers():
    """Test function with negative numbers"""
    assert two_sum([-1, -2, -3, -4], -7) == True
    assert two_sum([-5, 5, 10, -10], 0) == True

def test_two_sum_input_validation():
    """Test input validation and error handling"""
    with pytest.raises(TypeError, match="Input must be a list"):
        two_sum(123, 10)
    
    with pytest.raises(TypeError, match="All elements must be integers"):
        two_sum([1, 2, '3'], 6)
    
    with pytest.raises(ValueError, match="Input list must contain unique numbers"):
        two_sum([1, 2, 2, 3], 4)