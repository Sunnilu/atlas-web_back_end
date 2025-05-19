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

    # Dictionary to store session_id -> user_id mapping
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> Optional[str]:
        """
        Creates a session ID for a given user_id.

        Args:
            user_id (str): The ID of the user.

        Returns:
            str or None: The session ID if created, else None.
        """
        if user_id is None or not isinstance(user_id, str):
            return None

        session_id = str(uuid.uuid4())
        SessionAuth.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> Optional[str]:
        """
        Retrieves a user_id based on the session_id.

        Args:
            session_id (str): The session ID from the cookie.

        Returns:
            str or None: The user_id associated with the session, or None.
        """
        if session_id is None or not isinstance(session_id, str):
            return None

        return SessionAuth.user_id_by_session_id.get(session_id)

    def current_user(self, request=None) -> Optional[User]:
        """
        Retrieves the User instance based on the session cookie in the request.

        Args:
            request (flask.Request): The incoming request.

        Returns:
            User or None: The corresponding User instance, or None.
        """
        session_id = self.session_cookie(request)
        if session_id is None:
            return None

        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return None

        return User.get(user_id)

    def destroy_session(self, request=None) -> bool:
        """
        Deletes the session ID found in the request cookies (logs user out).

        Args:
            request (flask.Request): The incoming request.

        Returns:
            bool: True if session was successfully deleted, else False.
        """
        if request is None:
            return False

        session_id = self.session_cookie(request)
        if session_id is None:
            return False

        if self.user_id_for_session_id(session_id) is None:
            return False

        try:
            del SessionAuth.user_id_by_session_id[session_id]
        except KeyError:
            return False

        return True
