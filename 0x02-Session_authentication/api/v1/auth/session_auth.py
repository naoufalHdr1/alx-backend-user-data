#!/usr/bin/env python3
"""
SessionAuth module for managing session-based authentication.
"""
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """
    SessionAuth class inherits from Auth for session-based authentication.
    """
    # Class attribute for storing user_id by session_id
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ Creates a session ID for a given user_id.
        """
        if user_id is None or not isinstance(user_id, str):
            return None

        # Generate a unique session ID
        session_id = str(uuid.uuid4())

        # Store the user_id associated with the session ID
        self.user_id_by_session_id[session_id] = user_id

        return session_id
