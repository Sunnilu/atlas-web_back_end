#!/usr/bin/env python3
"""
SessionAuth module for handling session-based authentication.
"""

import uuid
from typing import Optional
from api.v1.auth.auth import Auth
from models.user import User


class SessionAuth(Auth):
    """
    SessionAuth class for managing in-memory session authentication.
    """

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> Optional[str]:
        """
        Creates a session ID for a user_id and stores it.

        Args:
            user_id (str): The ID of the user.

        Returns:
            str: The session ID, or None if invalid input.
        """
        if user_id is None or not isinstance(user_id, str):
            return None

        session_id = str(uuid.uuid4())
        SessionAuth.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> Optional[str]:
        """
        Retrieves the user ID associated with a session ID.

        Args:
            session_id (str): The session ID.

        Returns:
            str or None: The user ID, or None if not found.
        """
        if session_id is None or not isinstance(session_id, str):
            return None

        return SessionAuth.user_id_by_session_id.get(session_id)

    def current_user(self, request=None) -> Optional[User]:
        """
        Retrieves the User instance for session ID found in request cookie.

        Args:
            request (flask.Request): The request containing the cookie.

        Returns:
            User or None: The User instance if found, else None.
        """
        session_id = self.session_cookie(request)
        if session_id is None:
            return None

        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return None

        return User.get(user_id)
