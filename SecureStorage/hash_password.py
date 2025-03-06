import bcrypt

def hash_password(password):
    """
    Hash and salt the password using bcrypt.
    
    Args:
        password (str): The password to hash.
    
    Returns:
        str: The hashed password.
    """
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed.decode()  # Convert bytes to string for storage