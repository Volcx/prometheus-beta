import re

def count_unique_words(text):
    """
    Count the number of unique words in a given text, ignoring case and punctuation.
    
    Args:
        text (str): Input text to analyze
    
    Returns:
        int: Number of unique words in the text
    """
    # Convert to lowercase
    text = text.lower()
    
    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)
    
    # Split into words
    words = text.split()
    
    # Return count of unique words
    return len(set(words))