def two_sum(numbers, target):
    """
    Determine if any two unique numbers in the array sum to the target.
    
    Args:
        numbers (list): A list of unique integers
        target (int): The target sum to find
    
    Returns:
        bool: True if any two numbers in the array sum to the target, False otherwise
    
    Raises:
        TypeError: If input is not a list or if numbers are not integers
    """
    # Validate input types
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    # Validate that all elements are integers
    if not all(isinstance(num, int) for num in numbers):
        raise TypeError("All elements must be integers")
    
    # Use a set for O(n) time complexity
    seen = set()
    for num in numbers:
        complement = target - num
        if complement in seen:
            return True
        seen.add(num)
    
    return False