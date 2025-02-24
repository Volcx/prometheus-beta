import pytest
import requests
from src.website_checker import is_website_online

def test_valid_online_website():
    """Test that a known online website returns True."""
    assert is_website_online("https://www.google.com") == True

def test_invalid_url():
    """Test that an invalid URL raises a ValueError."""
    with pytest.raises(ValueError):
        is_website_online("")

def test_non_existent_website():
    """Test that a non-existent website returns False."""
    assert is_website_online("https://www.nonexistentwebsitexyz123.com") == False

def test_invalid_input_types():
    """Test that invalid input types raise a ValueError."""
    with pytest.raises(ValueError):
        is_website_online(123)
    with pytest.raises(ValueError):
        is_website_online(None)

def test_custom_timeout():
    """Test that custom timeout works."""
    # Use a very short timeout to simulate slow/unresponsive site
    assert is_website_online("https://www.google.com", timeout=0.01) == False