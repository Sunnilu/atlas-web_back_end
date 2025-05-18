#!/usr/bin/env python3
"""
BasicAuth module for handling Basic Authentication.
"""

import base64
from typing import TypeVar
from api.v1.auth.auth import Auth
from models.user import User


class BasicAuth(Auth):
    """ BasicAuth class that inherits from Auth. """

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """
        Extracts the Base64 part of the Authorization header for Basic Auth.

        Args:
            authorization_header (str): The full Authorization header.

        Returns:
            str or None: The Base64 encoded part of the header if valid,
                         else None.
        """
        if authorization_header is None:
            return None

        if not isinstance(authorization_header, str):
            return None

        if not authorization_header.startswith("Basic "):
            return None

        return authorization_header.split(' ', 1)[1]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """
        Decodes the Base64 string base64_authorization_header to UTF-8.

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

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """
        Extracts the user email and password from the decoded Base64 string.

        Args:
            decoded_base64_authorization_header (str): The decoded string.

        Returns:
            Tuple[str, str] or (None, None): email and password or (None, None)
        """
        if decoded_base64_authorization_header is None:
            return None, None

        if not isinstance(decoded_base64_authorization_header, str):
            return None, None

        if ':' not in decoded_base64_authorization_header:
            return None, None

        email, password = decoded_base64_authorization_header.split(':', 1)
        return email, password

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """
        Returns the User instance based on email and password.

        Args:
            user_email (str): The user email.
            user_pwd (str): The user password.

        Returns:
            User or None: The authenticated User instance, or None if invalid.
        """
        if user_email is None or not isinstance(user_email, str):
            return None

        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        try:
            users = User.search({"email": user_email})
        except Exception:
            return None

        if not users or not isinstance(users, list):
            return None

        user = users[0]

        if not user.is_valid_password(user_pwd):
            return None

        return user

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Retrieves the User instance for a given request using Basic Auth.

        Args:
            request (flask.Request): The Flask request object.

        Returns:
            User or None: The authenticated user or None if not valid.
        """
        if request is None:
            return None

        auth_header = self.authorization_header(request)
        if auth_header is None:
            return None

        b64_header = self.extract_base64_authorization_header(auth_header)
        if b64_header is None:
            return None

        decoded = self.decode_base64_authorization_header(b64_header)
        if decoded is None:
            return None

        email, password = self.extract_user_credentials(decoded)
        if email is None or password is None:
            return None

        return self.user_object_from_credentials(email, password)
