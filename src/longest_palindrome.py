def longest_palindromic_substring(s: str) -> str:
    """
    Find the longest palindromic substring within the given string.
    
    A palindrome is a string that reads the same backward as forward.
    
    Args:
        s (str): Input string to search for palindromic substrings
    
    Returns:
        str: The longest palindromic substring. 
             If multiple exist, returns the first occurrence.
             Returns an empty string if input is empty.
    
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    
    Examples:
        >>> longest_palindromic_substring("babad")
        'bab'
        >>> longest_palindromic_substring("cbbd")
        'bb'
        >>> longest_palindromic_substring("")
        ''
    """
    # Handle edge cases
    if not s:
        return ""
    
    start, max_length = 0, 1
    
    def expand_around_center(left: int, right: int) -> tuple:
        """
        Expand from center to find palindrome length and start index.
        
        Args:
            left (int): Left index to start expanding
            right (int): Right index to start expanding
        
        Returns:
            tuple: (start index of palindrome, length of palindrome)
        """
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        
        return left + 1, right - left - 1
    
    # Check all possible centers
    for i in range(len(s)):
        # Odd length palindromes
        odd_start, odd_length = expand_around_center(i, i)
        if odd_length > max_length:
            start = odd_start
            max_length = odd_length
        
        # Even length palindromes
        even_start, even_length = expand_around_center(i, i + 1)
        if even_length > max_length:
            start = even_start
            max_length = even_length
    
    return s[start:start + max_length]