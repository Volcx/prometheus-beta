def longest_subsequence_with_target_sum(arr, target):
    """
    Find the length of the longest subsequence in an array where the sum of elements equals the target.
    
    Args:
        arr (list): Input list of integers
        target (int): Target sum to match
    
    Returns:
        int: Length of the longest subsequence with sum equal to target. 
             Returns 0 if no such subsequence exists.
    
    Time Complexity: O(n * target)
    Space Complexity: O(target)
    
    Examples:
        >>> longest_subsequence_with_target_sum([1, 2, 3, 4, 5], 9)
        2
        >>> longest_subsequence_with_target_sum([1, 1, 1, 1], 3)
        3
        >>> longest_subsequence_with_target_sum([], 5)
        0
    """
    # Handle edge cases
    if not arr or target < 0:
        return 0
    
    # Initialize dynamic programming array
    # dp[j] represents the max length of subsequence with sum j
    dp = [0] * (target + 1)
    
    # Iterate through each number in the array
    for num in arr:
        # We create a copy to avoid modifying dp during iteration
        current_dp = dp.copy()
        
        # Check possibilities for each possible sum
        for j in range(target + 1):
            # If current sum is achievable
            if current_dp[j] >= 0:
                # Try to extend subsequence by current number
                new_sum = j + num
                
                # Update max length if new sum is within target
                if new_sum <= target:
                    dp[new_sum] = max(dp[new_sum], current_dp[j] + 1)
    
    # Return the maximum length found
    return max(dp)