#!/usr/bin/env python3
"""
Auth module for handling authentication templates.
"""

from typing import List, TypeVar
from flask import request


class Auth:
    """Template class for all authentication systems"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines whether authentication is required for a given path.

        Args:
            path (str): The path to check.
            excluded_paths (List[str]): List of paths that do not require auth.

        Returns:
            bool: True if authentication is required, False otherwise.
        """
        if path is None:
            return True

        if excluded_paths is None or not excluded_paths:
            return True

        # Normalize path to ensure trailing slash
        if not path.endswith('/'):
            path += '/'

        for excluded_path in excluded_paths:
            if excluded_path == path:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        Returns the Authorization header from the request.

        Args:
            request (flask.Request): The Flask request object.

        Returns:
            str or None: Authorization header if present, else None.
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Returns the current user based on the request.

        Args:
            request (flask.Request): The Flask request object.

        Returns:
            User or None: Currently authenticated user, or None.
        """
        return None
