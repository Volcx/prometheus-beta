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

    # Remove empty sub-arrays
    non_empty_arrays = [subarray for subarray in input_array if subarray]

    # Reverse elements in each sub-array
    reversed_arrays = [list(reversed(subarray)) for subarray in non_empty_arrays]

    # Flatten the array
    flattened = [item for subarray in reversed_arrays for item in subarray]

    # Remove duplicates while maintaining order
    seen = set()
    unique_items = []
    for item in flattened:
        if item not in seen:
            unique_items.append(item)
            seen.add(item)

    return unique_items