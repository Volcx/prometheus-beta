def count_palindromic_substrings(s: str) -> int:
    """
    Count the total number of palindromic substrings in a given string.
    
    A palindromic substring is a substring that reads the same forwards and backwards.
    
    Args:
        s (str): The input string to analyze
    
    Returns:
        int: Total number of palindromic substrings in the input string
    
    Examples:
        >>> count_palindromic_substrings("abc")
        3
        >>> count_palindromic_substrings("aaa")
        6
    
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    # Handle edge cases
    if not s:
        return 0
    
    # Total count of palindromic substrings
    total_count = 0
    
    # Helper function to expand around center
    def expand_around_center(left: int, right: int) -> int:
        count = 0
        # Expand while characters match and within string bounds
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
        return count
    
    # Iterate through all possible centers
    for i in range(len(s)):
        # Odd length palindromes (single character center)
        total_count += expand_around_center(i, i)
        
        # Even length palindromes (between two characters)
        total_count += expand_around_center(i, i + 1)
    
    return total_count