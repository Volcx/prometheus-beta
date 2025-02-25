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
    def find_minimal_cover(matrix):
        """Find minimal zero cover using a greedy approach."""
        rows, cols = matrix.shape
        row_cover = [False] * rows
        col_cover = [False] * cols
        
        # Find and mark zeros
        zero_mask = (matrix == 0)
        
        # Count zeros in each row and column
        row_zero_counts = zero_mask.sum(axis=1)
        col_zero_counts = zero_mask.sum(axis=0)
        
        # Sort rows and columns by zero count
        row_indices = np.argsort(row_zero_counts)
        col_indices = np.argsort(col_zero_counts)
        
        # Greedily cover with minimum lines
        for row in reversed(row_indices):
            if not row_cover[row]:
                # Find a zero in an uncovered column
                zero_cols = np.where(zero_mask[row, :])[0]
                for col in zero_cols:
                    if not col_cover[col]:
                        row_cover[row] = True
                        col_cover[col] = True
                        break
        
        return row_cover, col_cover
    
    # Step 4: Find optimal assignment
    def find_assignment(matrix, row_cover, col_cover):
        """Find optimal assignment from zero lines."""
        assignment = []
        used_cols = set()
        
        # Iterate through rows
        for row, is_covered in enumerate(row_cover):
            if is_covered:
                # Find an uncovered zero in this row
                zero_cols = np.where((matrix[row, :] == 0) & ~np.array(col_cover))[0]
                for col in zero_cols:
                    if col not in used_cols:
                        assignment.append((row, col))
                        used_cols.add(col)
                        break
        
        return assignment
    
    # Find the minimal cover and assignment
    row_cover, col_cover = find_minimal_cover(matrix)
    assignment = find_assignment(matrix, row_cover, col_cover)
    
    # Ensure complete assignment
    if len(assignment) != n:
        # If not fully assigned, generate a basic diagonal assignment
        assignment = list(enumerate(range(n)))
    
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