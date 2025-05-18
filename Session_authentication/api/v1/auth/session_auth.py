#!/usr/bin/env python3
"""
SessionAuth module for handling session-based authentication.
"""

import uuid
from typing import Optional
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """
    SessionAuth class for managing in-memory session authentication.
    """

    # Class attribute: maps session_id -> user_id
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> Optional[str]:
        """
        Creates a session ID for a user_id and stores it in the session dictionary.

        Args:
            user_id (str): The ID of the user to associate with the session.

        Returns:
            str or None: The newly created session ID, or None if invalid.
        """
        if user_id is None or not isinstance(user_id, str):
            return None

        session_id = str(uuid.uuid4())
        SessionAuth.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> Optional[str]:
        """
        Retrieves a user ID associated with the given session ID.

        Args:
            session_id (str): The session ID.

        Returns:
            str or None: The user ID if found, or None.
        """
        if session_id is None or not isinstance(session_id, str):
            return None

        return SessionAuth.user_id_by_session_id.get(session_id)

