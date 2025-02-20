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
    
    # Replace any non-alphanumeric character (except @ and #) with a space
    text = re.sub(r'[^a-z0-9@#\s]', ' ', text)
    
    # Split into words using multiple whitespaces as delimiter
    words = re.split(r'\s+', text.strip())
    
    # Remove any empty strings
    words = [word for word in words if word]
    
    # Return count of unique words
    return len(set(words))