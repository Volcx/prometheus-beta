import pytest
import time
from src.verification_code import VerificationCodeGenerator

def test_code_generation():
    """Test that generated code is a 6-digit string"""
    generator = VerificationCodeGenerator()
    code = generator.generate_code()
    
    assert len(code) == 6
    assert code.isdigit()

def test_unique_code_generation():
    """Test that multiple generated codes are unique"""
    generator = VerificationCodeGenerator()
    codes = set()
    
    for _ in range(100):
        code = generator.generate_code()
        assert code not in codes
        codes.add(code)

def test_code_validation():
    """Test code validation process"""
    generator = VerificationCodeGenerator()
    
    # Generate and validate a code
    code = generator.generate_code()
    assert generator.validate_code(code) == True
    
    # Validate same code again should return False (used code)
    assert generator.validate_code(code) == False

def test_code_expiration():
    """Test code expiration"""
    # Create generator with very short expiration time
    generator = VerificationCodeGenerator(expiration_time=1)
    
    code = generator.generate_code()
    
    # Wait for code to expire
    time.sleep(2)
    
    # Code should now be invalid
    assert generator.validate_code(code) == False

def test_invalid_code():
    """Test validation of invalid codes"""
    generator = VerificationCodeGenerator()
    
    # Random invalid code
    assert generator.validate_code('999999') == False
    
    # Empty string
    assert generator.validate_code('') == False
    
    # Non-digit code
    assert generator.validate_code('ABCDEF') == False