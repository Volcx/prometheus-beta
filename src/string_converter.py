def to_constant_case(input_string: str) -> str:
    """
    Convert a given string to constant case (ALL_UPPERCASE_WITH_UNDERSCORES).

    Args:
        input_string (str): The input string to be converted.

    Returns:
        str: The input string converted to constant case.

    Raises:
        TypeError: If the input is not a string.
    
    Examples:
        >>> to_constant_case("hello world")
        'HELLO_WORLD'
        >>> to_constant_case("thisIsATest")
        'THIS_IS_A_TEST'
        >>> to_constant_case("snake_case_string")
        'SNAKE_CASE_STRING'
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string
    if not input_string:
        return ""
    
    # Convert different cases to constant case
    # 1. Replace non-alphanumeric characters with underscores
    import re
    
    # First, handle camelCase and PascalCase by inserting underscores
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', input_string)
    s2 = re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1)
    
    # Replace any remaining non-alphanumeric characters with underscores
    cleaned = re.sub(r'[^a-zA-Z0-9]+', '_', s2)
    
    # Convert to uppercase and remove leading/trailing underscores
    return cleaned.strip('_').upper()