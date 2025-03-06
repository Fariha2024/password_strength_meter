import sqlite3
import json
from cryptography.fernet import Fernet

# Generate a key for encryption (store this securely in production)
key = Fernet.generate_key()
cipher_suite = Fernet(key)

def store_password_db(hashed_password, db_path="passwords.db"):
    """
    Store the hashed password in a SQLite database.
    
    Args:
        hashed_password (str): The hashed password to store.
        db_path (str): Path to the SQLite database file.
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS passwords (hash TEXT)")
    cursor.execute("INSERT INTO passwords (hash) VALUES (?)", (hashed_password,))
    conn.commit()
    conn.close()

def store_password_file(hashed_password, file_path="passwords.json"):
    """
    Store the hashed password in an encrypted JSON file.
    
    Args:
        hashed_password (str): The hashed password to store.
        file_path (str): Path to the JSON file.
    """
    data = {"hash": hashed_password}
    encrypted_data = cipher_suite.encrypt(json.dumps(data).encode())
    with open(file_path, "wb") as f:
        f.write(encrypted_data)