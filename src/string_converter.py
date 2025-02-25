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
    
    # Import regex and unidecode for unicode handling
    import re
    import unidecode
    
    # Normalize unicode characters
    input_string = unidecode.unidecode(input_string)
    
    # First, handle camelCase and PascalCase by inserting underscores
    # 1. Insert underscore between lowercase and uppercase letters
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', input_string)
    # 2. Insert underscore between lowercase/number and uppercase
    s2 = re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1)
    
    # 3. Insert underscore between number and letters
    s3 = re.sub('([a-zA-Z])([0-9])', r'\1_\2', s2)
    s4 = re.sub('([0-9])([a-zA-Z])', r'\1_\2', s3)
    
    # Replace any remaining non-alphanumeric characters with underscores
    cleaned = re.sub(r'[^a-zA-Z0-9]+', '_', s4)
    
    # Convert to uppercase, remove consecutive underscores, and strip edges
    return re.sub('_+', '_', cleaned.strip('_')).upper()