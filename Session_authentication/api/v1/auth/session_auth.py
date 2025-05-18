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

    # ✅ Class attribute (not instance!)
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
