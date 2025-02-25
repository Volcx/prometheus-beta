import numpy as np
import pytest
from src.hungarian_algorithm import hungarian_algorithm, calculate_total_cost

def test_basic_assignment():
    """Test a simple assignment problem."""
    cost_matrix = np.array([
        [3, 2, 3],
        [2, 1, 4],
        [4, 3, 1]
    ])
    assignment = hungarian_algorithm(cost_matrix)
    
    # Verify correct number of assignments
    assert len(assignment) == 3
    
    # Verify no row or column is repeated
    rows, cols = zip(*assignment)
    assert len(set(rows)) == 3
    assert len(set(cols)) == 3
    
    # Calculate and verify total cost
    total_cost = calculate_total_cost(cost_matrix, assignment)
    assert total_cost == 3  # The optimal assignment should have a total cost of 3

def test_rectangle_matrix_raises_error():
    """Test that non-square matrix raises ValueError."""
    cost_matrix = np.array([
        [1, 2, 3],
        [4, 5, 6]
    ])
    
    with pytest.raises(ValueError, match="Cost matrix must be square"):
        hungarian_algorithm(cost_matrix)

def test_non_numpy_input_raises_error():
    """Test that non-numpy input raises ValueError."""
    cost_matrix = [
        [1, 2],
        [3, 4]
    ]
    
    with pytest.raises(ValueError, match="Input must be a numpy array"):
        hungarian_algorithm(cost_matrix)

def test_non_2d_input_raises_error():
    """Test that non-2D input raises ValueError."""
    cost_matrix = np.array([1, 2, 3])
    
    with pytest.raises(ValueError, match="Input must be a 2D array"):
        hungarian_algorithm(cost_matrix)

def test_large_matrix():
    """Test a larger matrix."""
    cost_matrix = np.array([
        [82, 83, 69, 92],
        [77, 37, 49, 92],
        [11, 69, 5, 86],
        [8, 9, 98, 23]
    ])
    assignment = hungarian_algorithm(cost_matrix)
    
    # Verify correct number of assignments
    assert len(assignment) == 4
    
    # Verify no row or column is repeated
    rows, cols = zip(*assignment)
    assert len(set(rows)) == 4
    assert len(set(cols)) == 4
    
    # Calculate and verify total cost
    total_cost = calculate_total_cost(cost_matrix, assignment)
    assert total_cost <= 82  # Verify the lowest possible total cost

def test_all_same_cost():
    """Test a matrix where all costs are the same."""
    cost_matrix = np.ones((3, 3))
    assignment = hungarian_algorithm(cost_matrix)
    
    # Verify correct number of assignments
    assert len(assignment) == 3
    
    # Verify no row or column is repeated
    rows, cols = zip(*assignment)
    assert len(set(rows)) == 3
    assert len(set(cols)) == 3
    
    # Calculate and verify total cost
    total_cost = calculate_total_cost(cost_matrix, assignment)
    assert total_cost == 3  # Should be exactly 3 in this case