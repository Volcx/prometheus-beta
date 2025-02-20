def find_word_occurrences(text, target_word):
    """
    Find all occurrences of a target word in a given text.
    
    Args:
        text (str): The input text to search through
        target_word (str): The word to find occurrences of
    
    Returns:
        list: A list of tuples containing character position and word occurrence
    """
    # Validate inputs
    if not isinstance(text, str) or not isinstance(target_word, str):
        raise TypeError("Both text and target_word must be strings")
    
    if not text or not target_word:
        return []
    
    # Split the text into words
    words = text.split()
    
    # Track character position and results
    occurrences = []
    current_pos = 0
    
    for word in words:
        # Add space length if not the first word
        if current_pos > 0:
            current_pos += 1  # Add space between words
        
        # Check if current word matches target
        if word == target_word:
            occurrences.append((current_pos, word))
        
        # Update current position
        current_pos += len(word)
    
    return occurrences