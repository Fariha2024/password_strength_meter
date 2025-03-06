import re

def check_case(password):
    """
    Check if the password contains both uppercase and lowercase letters.
    
    Args:
        password (str): The password to check.
    
    Returns:
        bool: True if the password contains both uppercase and lowercase letters, False otherwise.
    """
    return bool(re.search(r'[A-Z]', password)) and bool(re.search(r'[a-z]', password))