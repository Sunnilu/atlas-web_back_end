#!/usr/bin/env python3
"""
BasicAuth module for handling Basic Authentication.
"""

from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """ BasicAuth class that inherits from Auth. """

    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """
        Extracts the Base64 part of the Authorization header for Basic Authentication.

        Args:
            authorization_header (str): The full Authorization header.

        Returns:
            str or None: The Base64 encoded part of the header if valid, else None.
        """
        if authorization_header is None:
            return None

        if not isinstance(authorization_header, str):
            return None

        if not authorization_header.startswith("Basic "):
            return None

        return authorization_header.split(' ', 1)[1]

    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        """
        Decodes the Base64 string base64_authorization_header to a UTF-8 string.

        Args:
            base64_authorization_header (str): The Base64 encoded string.

        Returns:
            str or None: The decoded UTF-8 string, or None if invalid.
        """
        if base64_authorization_header is None:
            return None

        if not isinstance(base64_authorization_header, str):
            return None

        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            return decoded_bytes.decode('utf-8')
        except (base64.binascii.Error, UnicodeDecodeError):
            return None
