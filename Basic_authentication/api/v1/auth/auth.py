from typing import List, TypeVar
from flask import request

class Auth:
    """
    Auth class to manage API authentication.
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if a path requires authentication. For now, it always returns False.
        
        :param path: The path requested.
        :param excluded_paths: A list of paths that do not require authentication.
        :return: False (authentication is not required)
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        Returns the authorization header from the request. For now, it always returns None.
        
        :param request: The Flask request object.
        :return: None (as no authorization header is implemented yet)
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Returns the current user from the request. For now, it always returns None.
        
        :param request: The Flask request object.
        :return: None (no user management is implemented yet)
        """
        return None
