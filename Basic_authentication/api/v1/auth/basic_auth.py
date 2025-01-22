#!/usr/bin/env python3
""" Basic authentication module
"""
import base64
from api.v1.auth.auth import Auth  # Assuming Auth class is defined in api.v1.auth.auth

class BasicAuth(Auth):
    """ BasicAuth class inherits from Auth.
    For now, it remains empty but can be extended in the future.
    """

    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """ Extracts the Base64 part of the Authorization header for Basic Authentication.

        Args:
            authorization_header (str): The Authorization header string.

        Returns:
            str: The Base64 part of the Authorization header, or None if invalid.
        """
        if authorization_header is None:
            return None
        
        if not isinstance(authorization_header, str):
            return None
        
        if not authorization_header.startswith("Basic "):
            return None
        
        # Return the part after "Basic "
        return authorization_header[6:]

    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        """ Decodes the Base64-encoded string into a UTF-8 string.

        Args:
            base64_authorization_header (str): The Base64-encoded string.

        Returns:
            str: The decoded value as a UTF-8 string, or None if invalid.
        """
        if base64_authorization_header is None:
            return None
        
        if not isinstance(base64_authorization_header, str):
            return None
        
        try:
            # Decode the Base64 string
            decoded_bytes = base64.b64decode(base64_authorization_header)
            # Decode bytes to a UTF-8 string
            return decoded_bytes.decode('utf-8')
        except (base64.binascii.Error, UnicodeDecodeError):
            # If decoding fails, return None
            return None
