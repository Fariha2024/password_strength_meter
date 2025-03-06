import secrets
import string

def generate_password(length=12, include_symbols=True):
    """
    Generate a strong, random password.
    
    Args:
        length (int): Length of the password (default is 12).
        include_symbols (bool): Whether to include symbols in the password (default is True).
    
    Returns:
        str: A strong, random password.
    """
    characters = string.ascii_letters + string.digits
    if include_symbols:
        characters += string.punctuation

    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password