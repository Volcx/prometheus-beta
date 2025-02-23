def remove_char_length(string: str, char: str) -> int:
    """
    Remove all instances of a specified character from a string and return its length.

    Args:
        string (str): The input string from which characters will be removed.
        char (str): The character to be removed from the input string.

    Returns:
        int: The length of the modified string after removing all occurrences 
             of the specified character.

    Raises:
        TypeError: If input is not a string.
        ValueError: If character to remove is not a single character.

    Examples:
        >>> remove_char_length("hello", "l")
        3
        >>> remove_char_length("python", "p")
        5
    """
    # Validate inputs
    if not isinstance(string, str):
        raise TypeError("Input must be a string")
    
    if not isinstance(char, str):
        raise TypeError("Character to remove must be a string")
    
    if len(char) != 1:
        raise ValueError("Character to remove must be a single character")
    
    # Remove the specified character and return the length
    return len(string.replace(char, ''))