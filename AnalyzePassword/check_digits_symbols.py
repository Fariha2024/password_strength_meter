import re

def check_digits_symbols(password):
    """
    Check if the password contains at least one digit and one special character.
    
    Args:
        password (str): The password to check.
    
    Returns:
        bool: True if the password contains a digit and a special character, False otherwise.
    """
    return bool(re.search(r'\d', password)) and bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))