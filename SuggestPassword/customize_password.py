from .generate_password import generate_password

def customize_password(length=12, include_symbols=True):
    """
    Generate a customized password based on user preferences.
    
    Args:
        length (int): Length of the password (default is 12).
        include_symbols (bool): Whether to include symbols in the password (default is True).
    
    Returns:
        str: A customized password.
    """
    return generate_password(length, include_symbols)