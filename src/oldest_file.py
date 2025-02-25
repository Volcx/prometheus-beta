import os
from typing import Union, Optional
from pathlib import Path

def find_oldest_file(directory: Union[str, Path]) -> Optional[str]:
    """
    Find the oldest file in a given directory.

    Args:
        directory (str or Path): Path to the directory to search.

    Returns:
        Optional[str]: Path to the oldest file, or None if no files exist.

    Raises:
        ValueError: If the directory does not exist or is not a directory.
    """
    # Convert to Path object for consistent handling
    dir_path = Path(directory)

    # Validate directory exists and is a directory
    if not dir_path.exists():
        raise ValueError(f"Directory does not exist: {dir_path}")
    
    if not dir_path.is_dir():
        raise ValueError(f"Provided path is not a directory: {dir_path}")

    # Get all files in the directory (excluding subdirectories)
    files = [f for f in dir_path.iterdir() if f.is_file()]

    # Return None if no files exist
    if not files:
        return None

    # Find the oldest file by creation time
    oldest_file = min(files, key=lambda f: f.stat().st_ctime)

    # Return the path as a string for compatibility
    return str(oldest_file)