def two_sum(nums: list[int], target: int) -> list[int]:
    """
    Find two numbers in the array that add up to the target.
    
    Args:
        nums: List of integers
        target: Target sum to find
        
    Returns:
        List of two indices whose corresponding numbers add up to target
        
    Example:
        >>> two_sum([2, 7, 11, 15], 9)
        [0, 1]
    """
    # Create a hash map to store number -> index mapping
    num_map = {}
    
    # Iterate through the array
    for i, num in enumerate(nums):
        # Calculate the complement needed
        complement = target - num
        
        # If complement exists in hash map, we found our pair
        if complement in num_map:
            return [num_map[complement], i]
            
        # Store current number and its index
        num_map[num] = i
    
    # No solution found (though problem states there will always be one)
    return [] 