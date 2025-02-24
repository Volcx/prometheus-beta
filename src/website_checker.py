import requests
import urllib3

def is_website_online(url: str, timeout: float = 5.0) -> bool:
    """
    Check if a website is online and accessible.

    Args:
        url (str): The full URL of the website to check (including http:// or https://)
        timeout (float, optional): Number of seconds to wait before timing out. Defaults to 5.0.

    Returns:
        bool: True if the website is online and responds, False otherwise.

    Raises:
        ValueError: If the URL is invalid or empty
    """
    # Validate input
    if not url or not isinstance(url, str):
        raise ValueError("URL must be a non-empty string")

    # Disable SSL warnings to prevent unnecessary console output
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    try:
        # Send a HEAD request to check the website
        # Use verify=False to allow self-signed certificates
        response = requests.head(url, timeout=timeout, verify=False)
        
        # Check if the response status code indicates success
        return 200 <= response.status_code < 400
    
    except (requests.ConnectionError, 
            requests.Timeout, 
            requests.RequestException):
        # Any connection or request error means the site is not online
        return False