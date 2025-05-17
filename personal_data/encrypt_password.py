#!/usr/bin/env python3
'''Encrypting passwords and validating the password'''


import bcrypt

def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Validates a password by comparing it against a stored hashed password.
    
    This function takes a password and compares it against a pre-hashed password using bcrypt's checkpw function.
    If the password matches the hashed version, it returns True, otherwise False.
    
    Args:
        hashed_password (bytes): The hashed password stored in the database.
        password (str): The plain-text password to check against the hashed password.
    
    Returns:
        bool: True if the password matches the hashed password, False otherwise.
    
    Example:
        is_valid(hashed_pw, "my_secure_password")
    """
    
    # Use bcrypt to check if the provided password matches the hashed password
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
