import pytest
import sys
from io import StringIO
from src.warning_logger import log_warning

def test_log_warning_normal_message(capsys):
    """Test logging a normal warning message."""
    log_warning("Test warning message")
    captured = capsys.readouterr()
    assert captured.err.strip() == "WARNING: Test warning message"

def test_log_warning_with_numbers(capsys):
    """Test logging a warning message with numbers."""
    log_warning("Warning with number 42")
    captured = capsys.readouterr()
    assert captured.err.strip() == "WARNING: Warning with number 42"

def test_log_warning_raise_type_error():
    """Test that TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Warning message must be a string"):
        log_warning(123)
    with pytest.raises(TypeError, match="Warning message must be a string"):
        log_warning(None)

def test_log_warning_raise_value_error():
    """Test that ValueError is raised for empty or whitespace-only messages."""
    with pytest.raises(ValueError, match="Warning message cannot be empty"):
        log_warning("")
    with pytest.raises(ValueError, match="Warning message cannot be empty"):
        log_warning("   \t\n")

def test_log_warning_unicode_message(capsys):
    """Test logging a warning message with unicode characters."""
    log_warning("Unicode warning: こんにちは")
    captured = capsys.readouterr()
    assert captured.err.strip() == "WARNING: Unicode warning: こんにちは"