"""
Provides a logging utility with support for indentation.
"""

class IndentedLogger:
    """
    A logger that supports message indentation and flexible logging.
    
    Attributes:
        _indent_level (int): Current indentation level.
        _indent_char (str): Character used for indentation.
        _indent_size (int): Number of indent characters per level.
    """
    
    def __init__(self, indent_char=' ', indent_size=4):
        """
        Initialize the IndentedLogger.
        
        Args:
            indent_char (str, optional): Character used for indentation. Defaults to space.
            indent_size (int, optional): Number of indent characters per level. Defaults to 4.
        
        Raises:
            ValueError: If indent_size is negative or indent_char is not a single character.
        """
        if indent_size < 0:
            raise ValueError("Indent size must be non-negative")
        
        if len(str(indent_char)) != 1:
            raise ValueError("Indent character must be a single character")
        
        self._indent_level = 0
        self._indent_char = str(indent_char)
        self._indent_size = indent_size
    
    def log(self, message):
        """
        Log a message with current indentation.
        
        Args:
            message (str): Message to log.
        
        Returns:
            str: Indented log message.
        """
        indent = self._indent_char * (self._indent_level * self._indent_size)
        return f"{indent}{message}"
    
    def indent(self):
        """
        Increase indentation level by 1.
        """
        self._indent_level += 1
    
    def unindent(self):
        """
        Decrease indentation level by 1, ensuring it doesn't go below 0.
        """
        self._indent_level = max(0, self._indent_level - 1)
    
    def reset_indent(self):
        """
        Reset indentation level to 0.
        """
        self._indent_level = 0
    
    @property
    def indent_level(self):
        """
        Get the current indentation level.
        
        Returns:
            int: Current indentation level.
        """
        return self._indent_level