import pytest
from src.sieve_of_eratosthenes import sieve_of_eratosthenes

def test_sieve_basic_cases():
    """Test basic functionality of the Sieve of Eratosthenes"""
    assert sieve_of_eratosthenes(10) == [2, 3, 5, 7]
    assert sieve_of_eratosthenes(2) == [2]
    assert sieve_of_eratosthenes(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

def test_edge_cases():
    """Test edge cases"""
    with pytest.raises(ValueError, match="Input must be greater than or equal to 2"):
        sieve_of_eratosthenes(1)
    
    with pytest.raises(ValueError, match="Input must be greater than or equal to 2"):
        sieve_of_eratosthenes(0)
    
    with pytest.raises(ValueError, match="Input must be greater than or equal to 2"):
        sieve_of_eratosthenes(-5)

def test_type_checks():
    """Test type checking"""
    with pytest.raises(TypeError, match="Input must be an integer"):
        sieve_of_eratosthenes(3.14)
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        sieve_of_eratosthenes("not a number")

def test_large_input():
    """Test with a larger input"""
    primes_up_to_100 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    assert sieve_of_eratosthenes(100) == primes_up_to_100