import os
import pathlib

def find_largest_file(directory):
    """
    Find the largest file in a given directory.

    Args:
        directory (str): Path to the directory to search.

    Returns:
        dict: A dictionary containing information about the largest file, with keys:
            - 'path': Full path to the largest file (str)
            - 'size': Size of the file in bytes (int)
            - 'name': Filename (str)

    Raises:
        TypeError: If directory is not a string.
        FileNotFoundError: If the directory does not exist.
        NotADirectoryError: If the provided path is not a directory.
    """
    # Input validation
    if not isinstance(directory, str):
        raise TypeError("Directory must be a string")
    
    # Convert to absolute path and validate directory
    dir_path = pathlib.Path(directory).resolve()
    
    if not dir_path.exists():
        raise FileNotFoundError(f"Directory does not exist: {directory}")
    
    if not dir_path.is_dir():
        raise NotADirectoryError(f"Provided path is not a directory: {directory}")
    
    # Find largest file
    largest_file = None
    largest_size = -1
    
    for entry in dir_path.iterdir():
        # Skip directories
        if entry.is_file():
            try:
                file_size = entry.stat().st_size
                if file_size > largest_size:
                    largest_file = entry
                    largest_size = file_size
            except (PermissionError, OSError):
                # Skip files that can't be accessed
                continue
    
    # Handle case of no files found
    if largest_file is None:
        return {
            'path': None,
            'size': 0,
            'name': None
        }
    
    return {
        'path': str(largest_file.resolve()),
        'size': largest_size,
        'name': largest_file.name
    }