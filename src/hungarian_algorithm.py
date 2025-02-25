import numpy as np
from scipy.optimize import linear_sum_assignment

def hungarian_algorithm(cost_matrix):
    """
    Implement the Hungarian algorithm for solving the assignment problem.
    
    Args:
        cost_matrix (np.ndarray): A 2D numpy array representing the cost matrix.
    
    Returns:
        list: A list of tuples representing the optimal assignment (row, col).
    
    Raises:
        ValueError: If the input is not a 2D numpy array or is not square.
    """
    # Input validation
    if not isinstance(cost_matrix, np.ndarray):
        raise ValueError("Input must be a numpy array")
    
    if cost_matrix.ndim != 2:
        raise ValueError("Input must be a 2D array")
    
    # Ensure square matrix
    if cost_matrix.shape[0] != cost_matrix.shape[1]:
        raise ValueError("Cost matrix must be square")
    
    # Use scipy's linear sum assignment for optimal solution
    row_ind, col_ind = linear_sum_assignment(cost_matrix)
    
    # Convert to list of tuples
    return list(zip(row_ind, col_ind))

def calculate_total_cost(cost_matrix, assignment):
    """
    Calculate the total cost of an assignment.
    
    Args:
        cost_matrix (np.ndarray): Original cost matrix
        assignment (list): List of (row, col) tuples representing assignment
    
    Returns:
        float: Total cost of the assignment
    """
    return sum(cost_matrix[row, col] for row, col in assignment)