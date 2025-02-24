def process_multidim_array(input_array):
    """
    Process a multi-dimensional array with the following operations:
    1. Remove empty sub-arrays
    2. Reverse the order of elements in each sub-array
    3. Flatten the array
    4. Remove duplicates while maintaining original order

    Args:
        input_array (list): A multi-dimensional list to be processed

    Returns:
        list: Processed array with specified transformations

    Raises:
        TypeError: If input is not a list
    """
    # Validate input
    if not isinstance(input_array, list):
        raise TypeError("Input must be a list")

    # Recursively flatten nested arrays
    def deep_flatten(arr):
        flattened = []
        for item in arr:
            if isinstance(item, list):
                flattened.extend(deep_flatten(item))
            else:
                flattened.append(item)
        return flattened

    # Reverse subarrays in original order, then slice to preserve reversal
    reversed_input = list(reversed(input_array))
    reversed_subarrays = [list(reversed(subarray)) for subarray in reversed_input if subarray]

    # Flatten and remove duplicates in order
    flattened = deep_flatten(reversed_subarrays)
    seen = set()
    unique_items = []
    for item in flattened:
        if item not in seen:
            unique_items.append(item)
            seen.add(item)

    return unique_items