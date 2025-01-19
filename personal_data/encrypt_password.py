#!/usr/bin/env python3
'''Encrypting passwords getting valid password'''


import bcrypt


def has_password(password:str) -> bytes:
    """ Description: Implement hash_password function one str argument
        returns a salted, hashed password, which is a byte string.
    """
     pass_encoded = password.encode()
    pass_hashed = bcrypt.hashpw(pass_encoded, bcrypt.gensalt())

    return pass_hashed  
