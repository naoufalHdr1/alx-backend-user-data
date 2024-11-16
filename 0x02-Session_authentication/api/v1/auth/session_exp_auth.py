#!/usr/bin/env python3
"""
SessionExpAuth module for managing session-based authentication with
expiration date.
"""
from api.v1.auth.session_auth import SessionAuth
from os import getenv
from datetime import datetime, timedelta


class SessionExpAuth(SessionAuth):
    """
    SessionAuth class inherits from Auth for session-based authentication.
    """
    # Class attribute for storing user_id by session_id
    user_id_by_session_id = {}

    def __init__(self):
        """ Initialize the session with a duration."""
        try:
            self.session_duration = int(getenv("SESSION_DURATION", 0))
        except ValueError:
            self.session_duration = 0

    def create_session(self, user_id: str = None) -> str:
        """ Create a session and store session metadata.
        """
        session_id = super().create_session(user_id)
        if session_id is None:
            return None

        self.user_id_by_session_id[session_id] = {
                "user_id": user_id,
                "created_at": datetime.now()
                }

        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ Retrieve a user ID based on session ID with expiration logic.
        """
        if session_id is None or not isinstance(session_id, str):
            return None

        session_dict = self.user_id_by_session_id.get(session_id)
        if session_dict is None:
            return None
        if "user_id" not in session_dict or "created_at" not in session_dict:
            return None

        if self.session_duration <= 0:
            return session_dict["user_id"]

        created_at = session_dict["created_at"]
        if not isinstance(created_at, datetime):
            return None

        expiry_time = created_at + timedelta(seconds=self.session_duration)
        if datetime.now() > expiry_time:
            return None

        return session_dict["user_id"]
