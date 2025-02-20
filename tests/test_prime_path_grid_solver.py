import pytest
from src.prime_path_grid_solver import find_prime_path, is_prime

def test_is_prime():
    # Test prime numbers
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(17) == True
    assert is_prime(29) == True
    
    # Test non-prime numbers
    assert is_prime(1) == False
    assert is_prime(4) == False
    assert is_prime(15) == False
    assert is_prime(100) == False

def test_find_prime_path_basic():
    # Grid with a prime path
    grid1 = [
        [1, 3, 5],
        [2, 7, 11],
        [13, 17, 19]
    ]
    path1 = find_prime_path(grid1)
    assert len(path1) > 1
    # Check all numbers in the path form a prime sequence
    sequence = [grid1[x][y] for x, y in path1]
    assert all(is_prime(int(''.join(map(str, sequence[:i+1])))) for i in range(len(sequence)))

def test_find_prime_path_no_solution():
    # Grid with no prime path
    grid2 = [
        [4, 6, 8],
        [10, 12, 14],
        [16, 18, 20]
    ]
    path2 = find_prime_path(grid2)
    assert path2 == []

def test_find_prime_path_edge_cases():
    # Empty grid
    assert find_prime_path([]) == []
    assert find_prime_path([[]]) == []

def test_find_prime_path_single_cell():
    # Single cell scenarios
    grid_single_prime = [[2]]
    grid_single_non_prime = [[4]]
    
    assert find_prime_path(grid_single_prime) == []
    assert find_prime_path(grid_single_non_prime) == []

def test_find_prime_path_large_prime_sequence():
    # Larger grid with potential for longer prime sequences
    grid3 = [
        [2, 3, 5, 7],
        [11, 13, 17, 19],
        [23, 29, 31, 37]
    ]
    path3 = find_prime_path(grid3)
    assert len(path3) > 1
    # Verify prime sequence creation
    sequence = [grid3[x][y] for x, y in path3]
    assert all(is_prime(int(''.join(map(str, sequence[:i+1])))) for i in range(len(sequence)))