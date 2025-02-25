def bead_sort(arr):
    """
    Implement the Bead Sort (Gravity Sort) algorithm for positive integers.
    
    Bead Sort is a natural sorting algorithm that works by simulating a physical 
    sorting process using beads on parallel rods. It is efficient for positive integers.
    
    Args:
        arr (list): A list of non-negative integers to be sorted.
    
    Returns:
        list: A new list with elements sorted in ascending order.
    
    Raises:
        ValueError: If the input contains negative numbers.
        TypeError: If input is not a list or contains non-integer elements.
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Check for non-integer or negative elements
    if any(not isinstance(x, int) or x < 0 for x in arr):
        raise ValueError("All elements must be non-negative integers")
    
    # Handle empty or single-element list
    if len(arr) <= 1:
        return list(arr)
    
    # Find the maximum number to determine the number of rods/columns
    max_num = max(arr)
    
    # Create a 2D representation of beads
    beads = []
    for num in arr:
        # Represent each number as a row of 'beads'
        beads.append([1] * num + [0] * (max_num - num))
    
    # Simulate gravity (dropping beads)
    for col in range(max_num):
        # Count 'beads' in each column from bottom to top
        col_count = sum(row[col] for row in beads)
        
        # Drop the beads to the bottom
        for row in range(len(beads)):
            # Set bottom beads first
            beads[row][col] = 1 if col_count > 0 else 0
            col_count -= beads[row][col]
    
    # Reconstruct the sorted list
    sorted_arr = [sum(row) for row in beads]
    
    return sorted_arr