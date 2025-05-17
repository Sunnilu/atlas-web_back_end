#!/usr/bin/env python3
"""
Encrypt password module
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hashes a password using bcrypt with a randomly generated salt.

    Args:
        password (str): The password to hash.

    Returns:
        bytes: The salted, hashed password.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Checks if the provided password matches the hashed password.
    
    Args:
        hashed_password (bytes): The hashed password.
        password (str): The plain-text password to verify.

    Returns:
        bool: True if the password is correct, False otherwise.
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
