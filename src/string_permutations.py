def generate_unique_permutations(s):
    """
    Generate all unique permutations of a given string.
    
    Args:
        s (str): Input string to generate permutations for.
    
    Returns:
        list: A list of unique permutations of the input string.
    
    Raises:
        TypeError: If input is not a string.
    """
    # Validate input 
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    # Special cases
    if not s:
        return []
    
    # Convert to list for manipulation and sort to ensure consistent ordering
    chars = sorted(s)
    
    def backtrack(current_perm, remaining_chars):
        # Base case: if no chars remain, we have a complete permutation
        if not remaining_chars:
            return [current_perm]
        
        # Set to track unique permutations at this step
        unique_perms = []
        used_chars = set()
        
        # Try each remaining character
        for i in range(len(remaining_chars)):
            # Skip duplicates to ensure unique permutations
            if remaining_chars[i] in used_chars:
                continue
            
            # Mark this character as used
            used_chars.add(remaining_chars[i])
            
            # Recursive permutation generation
            new_perm = current_perm + remaining_chars[i]
            new_remaining = remaining_chars[:i] + remaining_chars[i+1:]
            
            # Extend permutations list
            unique_perms.extend(backtrack(new_perm, new_remaining))
        
        return unique_perms
    
    # Generate and return all unique permutations
    return backtrack('', chars)