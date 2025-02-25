import os
import tempfile
import pytest
from pathlib import Path
import time

from src.oldest_file import find_oldest_file

def test_find_oldest_file_basic():
    """Test finding the oldest file in a directory."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create three files with deliberate time differences
        file1 = Path(tmpdir) / 'file1.txt'
        file2 = Path(tmpdir) / 'file2.txt'
        file3 = Path(tmpdir) / 'file3.txt'
        
        # Create files with slightly different creation times
        file1.touch()
        time.sleep(0.1)
        file2.touch()
        time.sleep(0.1)
        file3.touch()
        
        # Find the oldest file
        oldest = find_oldest_file(tmpdir)
        
        # Verify it's the first file created
        assert oldest == str(file1)

def test_find_oldest_file_empty_directory():
    """Test behavior when directory is empty."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Should return None for an empty directory
        assert find_oldest_file(tmpdir) is None

def test_find_oldest_file_nonexistent_directory():
    """Test error handling for non-existent directory."""
    with pytest.raises(ValueError, match="Directory does not exist"):
        find_oldest_file('/path/to/nonexistent/directory')

def test_find_oldest_file_not_a_directory():
    """Test error handling when path is not a directory."""
    with tempfile.NamedTemporaryFile() as temp_file:
        with pytest.raises(ValueError, match="is not a directory"):
            find_oldest_file(temp_file.name)

def test_find_oldest_file_with_path_object():
    """Test that the function works with Path objects."""
    with tempfile.TemporaryDirectory() as tmpdir:
        temp_path = Path(tmpdir)
        file1 = temp_path / 'file1.txt'
        file2 = temp_path / 'file2.txt'
        
        file1.touch()
        time.sleep(0.1)
        file2.touch()
        
        oldest = find_oldest_file(temp_path)
        assert oldest == str(file1)

def test_find_oldest_file_ignores_subdirectories():
    """Ensure the function only considers files, not subdirectories."""
    with tempfile.TemporaryDirectory() as tmpdir:
        temp_path = Path(tmpdir)
        file1 = temp_path / 'file1.txt'
        subdir = temp_path / 'subdir'
        
        file1.touch()
        subdir.mkdir()
        
        oldest = find_oldest_file(tmpdir)
        assert oldest == str(file1)