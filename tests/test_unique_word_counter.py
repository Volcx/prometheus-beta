import pytest
from src.unique_word_counter import count_unique_words

def test_basic_unique_words():
    """Test basic unique word counting"""
    assert count_unique_words("hello world hello") == 2

def test_case_insensitive():
    """Test that word counting is case-insensitive"""
    assert count_unique_words("Hello HELLO hello") == 1

def test_punctuation_handling():
    """Test that punctuation is ignored"""
    assert count_unique_words("hello, world! Hello.") == 2

def test_empty_string():
    """Test handling of empty string"""
    assert count_unique_words("") == 0

def test_complex_text():
    """Test with a more complex text"""
    text = "The quick brown fox jumps over the lazy dog. The fox is quick!"
    assert count_unique_words(text) == 7

def test_special_characters():
    """Test handling of strings with special characters"""
    assert count_unique_words("hello@world hello#world") == 2