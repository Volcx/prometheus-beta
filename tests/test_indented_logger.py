"""
Tests for the IndentedLogger class.
"""

import pytest
from src.indented_logger import IndentedLogger

def test_basic_logging():
    """Test basic logging functionality."""
    logger = IndentedLogger()
    assert logger.log("Hello") == "Hello"

def test_indent_increases_indentation():
    """Test that indent increases indentation level."""
    logger = IndentedLogger()
    logger.indent()
    assert logger.log("Indented") == "    Indented"
    logger.indent()
    assert logger.log("Double Indented") == "        Double Indented"

def test_unindent_decreases_indentation():
    """Test that unindent decreases indentation level."""
    logger = IndentedLogger()
    logger.indent()
    logger.indent()
    logger.unindent()
    assert logger.log("Single Indented") == "    Single Indented"

def test_unindent_prevents_negative_indentation():
    """Test that unindent doesn't go below 0."""
    logger = IndentedLogger()
    logger.unindent()
    assert logger.log("No Indentation") == "No Indentation"

def test_reset_indent():
    """Test reset_indent method."""
    logger = IndentedLogger()
    logger.indent()
    logger.indent()
    logger.reset_indent()
    assert logger.log("Reset") == "Reset"

def test_custom_indent_char():
    """Test custom indent character."""
    logger = IndentedLogger(indent_char='-')
    logger.indent()
    assert logger.log("Dashed") == "----Dashed"

def test_custom_indent_size():
    """Test custom indent size."""
    logger = IndentedLogger(indent_size=2)
    logger.indent()
    assert logger.log("Custom Size") == "  Custom Size"

def test_invalid_indent_char():
    """Test that multiple-character indent_char raises an error."""
    with pytest.raises(ValueError, match="Indent character must be a single character"):
        IndentedLogger(indent_char='--')

def test_negative_indent_size():
    """Test that negative indent_size raises an error."""
    with pytest.raises(ValueError, match="Indent size must be non-negative"):
        IndentedLogger(indent_size=-1)

def test_indent_level_property():
    """Test the indent_level property."""
    logger = IndentedLogger()
    assert logger.indent_level == 0
    logger.indent()
    assert logger.indent_level == 1
    logger.indent()
    assert logger.indent_level == 2
    logger.unindent()
    assert logger.indent_level == 1
    logger.reset_indent()
    assert logger.indent_level == 0