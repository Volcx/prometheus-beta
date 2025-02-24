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

    # Remove empty sub-arrays and flatten
    flattened = deep_flatten([subarray for subarray in input_array if subarray])

    # Reverse the flattened list
    flattened_reversed = list(reversed(flattened))

    # Remove duplicates while maintaining order
    seen = set()
    unique_items = []
    for item in flattened_reversed:
        if item not in seen:
            unique_items.append(item)
            seen.add(item)

    return unique_items