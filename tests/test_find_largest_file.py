import os
import pytest
import tempfile
import pathlib

from src.find_largest_file import find_largest_file

def test_find_largest_file_basic():
    """Test finding the largest file in a directory."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create test files
        paths = [
            os.path.join(tmpdir, 'small.txt'),
            os.path.join(tmpdir, 'medium.txt'),
            os.path.join(tmpdir, 'large.txt')
        ]
        
        # Write files with different sizes
        with open(paths[0], 'w') as f:
            f.write('small')
        
        with open(paths[1], 'w') as f:
            f.write('medium' * 10)
        
        with open(paths[2], 'w') as f:
            f.write('large' * 100)
        
        # Find largest file
        result = find_largest_file(tmpdir)
        
        # Verify result
        assert result['name'] == 'large.txt'
        assert result['size'] == len('large' * 100)
        assert result['path'] == str(pathlib.Path(paths[2]).resolve())

def test_find_largest_file_empty_dir():
    """Test behavior with an empty directory."""
    with tempfile.TemporaryDirectory() as tmpdir:
        result = find_largest_file(tmpdir)
        
        assert result['path'] is None
        assert result['size'] == 0
        assert result['name'] is None

def test_find_largest_file_error_handling():
    """Test error handling for invalid inputs."""
    # Non-string input
    with pytest.raises(TypeError):
        find_largest_file(123)
    
    # Non-existent directory
    with pytest.raises(FileNotFoundError):
        find_largest_file('/path/to/nonexistent/directory')
    
    # Not a directory
    with tempfile.TemporaryDirectory() as tmpdir:
        temp_file = os.path.join(tmpdir, 'temp.txt')
        with open(temp_file, 'w') as f:
            f.write('test')
        
        with pytest.raises(NotADirectoryError):
            find_largest_file(temp_file)

def test_find_largest_file_with_similar_sized_files():
    """Test finding largest file when multiple files have similar sizes."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create files with close sizes
        paths = [
            os.path.join(tmpdir, 'file1.txt'),
            os.path.join(tmpdir, 'file2.txt'),
            os.path.join(tmpdir, 'file3.txt')
        ]
        
        with open(paths[0], 'w') as f:
            f.write('a' * 50)
        
        with open(paths[1], 'w') as f:
            f.write('b' * 49)
        
        with open(paths[2], 'w') as f:
            f.write('c' * 51)
        
        # Find largest file
        result = find_largest_file(tmpdir)
        
        # Verify result
        assert result['name'] == 'file3.txt'
        assert result['size'] == 51