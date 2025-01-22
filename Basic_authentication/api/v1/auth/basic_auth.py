#!/usr/bin/env python3
""" Basic authentication module
"""
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
