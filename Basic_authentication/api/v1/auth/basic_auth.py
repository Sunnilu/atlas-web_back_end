#!/usr/bin/env python3
""" Basic authentication module
"""
from typing import TypeVar
from api.v1.auth.auth import Auth  # Assuming Auth class is defined in api.v1.auth.auth
from models.user import User  # Assuming User class is defined in models.user

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

    def extract_user_credentials(self, decoded_base64_authorization_header: str) -> (str, str):
        """ Extracts the user email and password from the decoded Base64 string.

        Args:
            decoded_base64_authorization_header (str): The decoded Base64 string in the format email:password.

        Returns:
            tuple: A tuple containing email and password, or (None, None) if invalid.
        """
        if decoded_base64_authorization_header is None:
            return None, None
        
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        
        if ':' not in decoded_base64_authorization_header:
            return None, None
        
        # Split the string into email and password using the first ":"
        email, password = decoded_base64_authorization_header.split(":", 1)
        return email, password

    def user_object_from_credentials(self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """ Returns the User instance based on user_email and user_pwd.

        Args:
            user_email (str): The user's email.
            user_pwd (str): The user's password.

        Returns:
            User: The User instance if valid credentials are provided, or None if invalid.
        """
        # Validate inputs
        if not isinstance(user_email, str) or user_email is None:
            return None
        
        if not isinstance(user_pwd, str) or user_pwd is None:
            return None

        # Use the User.search method to search for a user by email
        users = User.search({"email": user_email})
        
        # If no user is found, return None
        if not users:
            return None
        
        # Get the first matching user (assuming email is unique)
        user = users[0]

        # Check if the provided password is valid for the user
        if not user.is_valid_password(user_pwd):
            return None

        # Return the User instance
        return user

    def current_user(self, request=None) -> TypeVar('User'):
        """ Retrieves the User instance for the request, based on Basic Authentication.

        Args:
            request (Request): The Flask request object.

        Returns:
            User: The authenticated User instance, or None if authentication fails.
        """
        # Retrieve the Authorization header from the request
        authorization_header = request.headers.get("Authorization")

        # Extract the Base64 part of the authorization header
        base64_authorization_header = self.extract_base64_authorization_header(authorization_header)
        if base64_authorization_header is None:
            return None

        # Decode the Base64 part into a UTF-8 string
        decoded_base64_authorization_header = self.decode_base64_authorization_header(base64_authorization_header)
        if decoded_base64_authorization_header is None:
            return None

        # Extract the user credentials (email and password) from the decoded string
        user_email, user_pwd = self.extract_user_credentials(decoded_base64_authorization_header)
        if user_email is None or user_pwd is None:
            return None

        # Retrieve the User object based on email and password
        user = self.user_object_from_credentials(user_email, user_pwd)
        return user
