import pytest
from src.word_occurrence_finder import find_word_occurrences

def test_basic_occurrence():
    text = "the quick brown fox jumps over the lazy dog"
    assert find_word_occurrences(text, "the") == [(0, "the"), (31, "the")]

def test_single_word():
    text = "hello"
    assert find_word_occurrences(text, "hello") == [(0, "hello")]

def test_no_occurrences():
    text = "quick brown fox"
    assert find_word_occurrences(text, "jumps") == []

def test_empty_inputs():
    assert find_word_occurrences("", "word") == []
    assert find_word_occurrences("hello world", "") == []

def test_invalid_inputs():
    with pytest.raises(TypeError):
        find_word_occurrences(None, "word")
    with pytest.raises(TypeError):
        find_word_occurrences("text", None)

def test_complex_text():
    text = "hello hello world hello"
    assert find_word_occurrences(text, "hello") == [(0, "hello"), (6, "hello"), (18, "hello")]

def test_case_sensitive():
    text = "Hello hello HELLO"
    assert find_word_occurrences(text, "hello") == [(6, "hello")]