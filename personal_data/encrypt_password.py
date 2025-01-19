#!/usr/bin/env python3
'''Encrypting passwords and validating the password'''

import bcrypt

def has_password(password: str) -> bytes:
    """ 
    Description: Implement hash_password function with one str argument
    Returns a salted, hashed password, which is a byte string.
    Uses bcrypt package to perform the hashing (with hashpw).
    """
    pass_encoded: bytes = password.encode()  # Encoded password as bytes
    pass_hashed: bytes = bcrypt.hashpw(pass_encoded, bcrypt.gensalt())  # Hashed password as bytes
    return pass_hashed  # Return type is bytes

def is_valid(hashed_password: bytes, password: str) -> bool:
    '''
    Description: Implement an is_valid function that expects 2 arguments and
                 returns a boolean.
    Arguments:   
        hashed_password: bytes type
        password: string type
    Use bcrypt to validate that the provided password matches the hashed password.
    '''
    pass_encoded: bytes = password.encode()  # Encoded password as bytes
    return bcrypt.checkpw(pass_encoded, hashed_password)  # Returns True or False
