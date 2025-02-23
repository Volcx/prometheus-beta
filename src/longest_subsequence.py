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
    
    # Use dynamic programming to track subsequence lengths
    dp = [0] * (target + 1)
    
    for num in arr:
        # Create a copy to avoid modifying while iterating
        current_dp = dp.copy()
        
        for j in range(target + 1):
            # If current sum is achievable
            if j == num:
                # Single element match
                dp[j] = max(dp[j], 1)
            elif j > num and current_dp[j - num] > 0:
                # Extend existing subsequence
                dp[j] = max(dp[j], current_dp[j - num] + 1)
        
    return max(dp)