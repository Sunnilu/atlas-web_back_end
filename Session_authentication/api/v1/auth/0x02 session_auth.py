#!/usr/bin/env python3
"""
SessionAuth module for handling session-based authentication.
"""

import uuid
from typing import Optional
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """
    SessionAuth class that inherits from Auth.
    Handles creation and storage of in-memory session IDs.
    """

    # Class attribute for storing session_id -> user_id mappings
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> Optional[str]:
        """
        Creates a session ID for a given user_id.

        Args:
            user_id (str): The ID of the user to associate with the session.

        Returns:
            str or None: The session ID if successful, otherwise None.
        """
        if user_id is None or not isinstance(user_id, str):
            return None

        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id
