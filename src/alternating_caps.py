def to_alternating_caps(input_string):
    """
    Convert a string to alternating capitalization.

    Args:
        input_string (str): The input string to convert.

    Returns:
        str: A string with alternating capitalization.

    Raises:
        TypeError: If input is not a string.
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string case
    if not input_string:
        return ""
    
    # Convert to alternating caps, maintaining alternation per word
    result = []
    for word in input_string.split():
        word_result = []
        upper_turn = True
        for char in word:
            if char.isalpha():
                word_result.append(char.upper() if upper_turn else char.lower())
                upper_turn = not upper_turn
            else:
                word_result.append(char)
        result.append(''.join(word_result))
    
    return ' '.join(result)