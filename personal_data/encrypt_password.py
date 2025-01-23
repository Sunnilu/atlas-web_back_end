#!/usr/bin/env python3
'''Encrypting passwords and validating the password'''

import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hashes a given password using bcrypt with a randomly generated salt.

    This function will take a plain-text password, encode it to bytes,
    generate a salt, and then return the hashed password as a byte string.

    Args:
        password (str): The password to be hashed, provided as a string.

    Returns:
        bytes: The salted and hashed password, returned as a byte string.

    Example:
        hashed_pw = hash_password("my_secure_password")
    """

    # Generate a salt for bcrypt, using the default cost factor
    salt = bcrypt.gensalt()

    # Hash the password using bcrypt and the generated salt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    # Return the hashed password as a byte string
    return hashed_password
