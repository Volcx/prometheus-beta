def run_length_encode(data):
    """
    Implement Run-Length Encoding (RLE) compression for a given input.
    
    Args:
        data (str or list): The input data to be compressed.
    
    Returns:
        list: Compressed data in the format [value, count].
    
    Raises:
        TypeError: If input is not a string or list.
        ValueError: If input is an empty sequence.
    """
    # Validate input
    if not isinstance(data, (str, list)):
        raise TypeError("Input must be a string or list")
    
    if not data:
        raise ValueError("Input cannot be empty")
    
    # Convert string to list if needed
    if isinstance(data, str):
        data = list(data)
    
    # Perform Run-Length Encoding
    compressed = []
    if not data:
        return compressed
    
    current_item = data[0]
    current_count = 1
    
    for item in data[1:]:
        if item == current_item:
            current_count += 1
        else:
            compressed.append([current_item, current_count])
            current_item = item
            current_count = 1
    
    # Add the last run
    compressed.append([current_item, current_count])
    
    return compressed

def run_length_decode(compressed_data):
    """
    Decode Run-Length Encoded data back to its original form.
    
    Args:
        compressed_data (list): Compressed data in the format [value, count].
    
    Returns:
        list: Decompressed data.
    
    Raises:
        TypeError: If input is not a list or contains invalid elements.
        ValueError: If input is empty or contains invalid count values.
    """
    # Validate input
    if not isinstance(compressed_data, list):
        raise TypeError("Input must be a list")
    
    if not compressed_data:
        raise ValueError("Input cannot be empty")
    
    # Perform Run-Length Decoding
    decompressed = []
    
    for item, count in compressed_data:
        # Validate each compressed item
        if not isinstance(count, int) or count < 1:
            raise ValueError(f"Invalid count: {count}. Count must be a positive integer.")
        
        # Extend the decompressed list with repeated items
        decompressed.extend([item] * count)
    
    return decompressed