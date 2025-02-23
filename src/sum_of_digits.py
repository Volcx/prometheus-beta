def sum_of_digits(input_string: str) -> int:
    """
    Calculate the sum of digits in a given string.
    
    Args:
        input_string (str): A string potentially containing digits.
    
    Returns:
        int: The sum of all digits in the string, ignoring leading zeros.
    
    Examples:
        >>> sum_of_digits('1234567890')
        45
        >>> sum_of_digits('abc123')
        6
        >>> sum_of_digits('')
        0
        >>> sum_of_digits('hello')
        0
    """
    # Extract only digit characters and convert to integers
    digits = [int(char) for char in input_string if char.isdigit()]
    
    # Return the sum of digits
    return sum(digits)