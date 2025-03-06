def check_length(password, min_length=8):
    """
    Check if the password meets the minimum length requirement.
    
    Args:
        password (str): The password to check.
        min_length (int): Minimum required length (default is 8).
    
    Returns:
        bool: True if the password meets the length requirement, False otherwise.
    """
    return len(password) >= min_length