common_passwords = ["password", "123456", "qwerty", "admin"]

def is_password_blacklisted(password):
    """
    Check if the password is in the list of common passwords.
    
    Args:
        password (str): The password to check.
    
    Returns:
        bool: True if the password is not blacklisted, False otherwise.
    """
    return password.lower() not in common_passwords