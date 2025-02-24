import sys

def log_warning(message):
    """
    Log a warning message to the console on stderr.

    Args:
        message (str): The warning message to be logged.

    Raises:
        TypeError: If the message is not a string.
        ValueError: If the message is an empty string.
    """
    # Validate input
    if not isinstance(message, str):
        raise TypeError("Warning message must be a string")
    
    if not message.strip():
        raise ValueError("Warning message cannot be empty")
    
    # Print warning message to stderr
    print(f"WARNING: {message}", file=sys.stderr)