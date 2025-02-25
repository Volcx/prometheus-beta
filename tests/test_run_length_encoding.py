import pytest
from src.run_length_encoding import run_length_encode, run_length_decode

def test_rle_encode_string():
    """Test RLE encoding with a string input."""
    input_data = "AABBBCCCC"
    expected = [['A', 2], ['B', 3], ['C', 4]]
    assert run_length_encode(input_data) == expected

def test_rle_encode_list():
    """Test RLE encoding with a list input."""
    input_data = ['A', 'A', 'B', 'B', 'B', 'C', 'C', 'C', 'C']
    expected = [['A', 2], ['B', 3], ['C', 4]]
    assert run_length_encode(input_data) == expected

def test_rle_decode_basic():
    """Test RLE decoding of basic compressed data."""
    input_data = [['A', 2], ['B', 3], ['C', 4]]
    expected = ['A', 'A', 'B', 'B', 'B', 'C', 'C', 'C', 'C']
    assert run_length_decode(input_data) == expected

def test_rle_encode_single_char():
    """Test RLE encoding with a single character."""
    input_data = "AAAAA"
    expected = [['A', 5]]
    assert run_length_encode(input_data) == expected

def test_rle_encode_no_repetition():
    """Test RLE encoding with no repeated characters."""
    input_data = "ABCDE"
    expected = [['A', 1], ['B', 1], ['C', 1], ['D', 1], ['E', 1]]
    assert run_length_encode(input_data) == expected

def test_rle_decode_single_run():
    """Test RLE decoding with a single run."""
    input_data = [['X', 5]]
    expected = ['X', 'X', 'X', 'X', 'X']
    assert run_length_decode(input_data) == expected

def test_rle_encode_empty_input_error():
    """Test error handling for empty input during encoding."""
    with pytest.raises(ValueError, match="Input cannot be empty"):
        run_length_encode("")

def test_rle_decode_empty_input_error():
    """Test error handling for empty input during decoding."""
    with pytest.raises(ValueError, match="Input cannot be empty"):
        run_length_decode([])

def test_rle_encode_invalid_type_error():
    """Test error handling for invalid input type during encoding."""
    with pytest.raises(TypeError, match="Input must be a string or list"):
        run_length_encode(12345)

def test_rle_decode_invalid_type_error():
    """Test error handling for invalid input type during decoding."""
    with pytest.raises(TypeError, match="Input must be a list"):
        run_length_decode("not a list")

def test_rle_decode_invalid_count_error():
    """Test error handling for invalid count values during decoding."""
    with pytest.raises(ValueError, match="Invalid count"):
        run_length_decode([['A', -1]])
    with pytest.raises(ValueError, match="Invalid count"):
        run_length_decode([['A', 0]])

def test_rle_roundtrip():
    """Test complete roundtrip encoding and decoding."""
    original = "AABBCCCDDDDEEEEE"
    encoded = run_length_encode(original)
    decoded = run_length_decode(encoded)
    assert ''.join(decoded) == original