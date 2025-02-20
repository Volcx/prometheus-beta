import random
import string
import time

class VerificationCodeGenerator:
    def __init__(self, expiration_time=300):  # 5 minutes default expiration
        self._generated_codes = {}
        self._expiration_time = expiration_time

    def generate_code(self):
        """
        Generate a unique 6-digit verification code.
        
        Returns:
            str: A unique 6-digit verification code
        """
        # Clean up expired codes
        current_time = time.time()
        self._generated_codes = {
            code: timestamp for code, timestamp in self._generated_codes.items()
            if current_time - timestamp < self._expiration_time
        }
        
        # Generate a unique code
        while True:
            # Generate a 6-digit code using digits only
            code = ''.join(random.choices(string.digits, k=6))
            
            # Ensure the code is unique
            if code not in self._generated_codes:
                self._generated_codes[code] = current_time
                return code

    def validate_code(self, code):
        """
        Validate a verification code.
        
        Args:
            code (str): The verification code to validate
        
        Returns:
            bool: True if the code is valid and not expired, False otherwise
        """
        current_time = time.time()
        
        # Check if code exists and is not expired
        if (code in self._generated_codes and 
            current_time - self._generated_codes[code] < self._expiration_time):
            # Optional: Remove the code after successful validation
            del self._generated_codes[code]
            return True
        
        return False