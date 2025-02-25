import numpy as np

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
    
    # Create a working copy of the cost matrix
    matrix = cost_matrix.copy().astype(float)
    n = matrix.shape[0]
    
    # Step 1: Subtract row minimums
    for i in range(n):
        matrix[i] -= matrix[i].min()
    
    # Step 2: Subtract column minimums
    for j in range(n):
        matrix[:, j] -= matrix[:, j].min()
    
    # Step 3: Cover zeros with minimal number of lines
    covered_rows = set()
    covered_cols = set()
    
    while len(covered_rows) + len(covered_cols) < n:
        # Find uncovered zeros
        zero_mask = (matrix == 0)
        zero_row_counts = (~covered_rows).dot(zero_mask)
        zero_col_counts = zero_mask.dot(~covered_cols.T)
        
        # Find the row/column with most uncovered zeros
        if zero_row_counts.max() > zero_col_counts.max():
            row = zero_row_counts.argmax()
            covered_rows.add(row)
            
            # Cover columns of zeros in this row
            zero_cols = np.where(zero_mask[row])[0]
            covered_cols.update(zero_cols)
        else:
            col = zero_col_counts.argmax()
            covered_cols.add(col)
            
            # Cover rows with zeros in this column
            zero_rows = np.where(zero_mask[:, col])[0]
            covered_rows.update(zero_rows)
    
    # Step 4: Find optimal assignment
    assignment = []
    for i in range(n):
        for j in range(n):
            if matrix[i, j] == 0 and j not in [x[1] for x in assignment]:
                assignment.append((i, j))
                break
    
    return assignment

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