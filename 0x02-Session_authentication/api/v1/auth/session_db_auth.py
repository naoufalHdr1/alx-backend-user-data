#!/user/bin/env python3
""" Session authentication with expiration and storage support module
for the API.
"""
from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession
from datetime import datetime, timedelta


class SessionDBAuth(SessionExpAuth):
    """ Session authentication with database support. """

    def create_session(self, user_id: str = None) -> str:
        """ Create a session and store it in the database. """
        session_id = super().create_session(user_id)
        if not session_id:
            return None

        # Create a UserSession instance
        user_session = UserSession(user_id=user_id, session_id=session_id)
        user_session.save()
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ Retrieve user ID from the database based on session_id. """
        if not session_id:
            return None

        # Search for the session using the `search` method
        session = UserSession.search({'session_id': session_id})[0]
        if not session:
            return None

        if self.session_duration <= 0:
            return session.user_id

        created_at = session.created_at
        if not created_at or not isinstance(created_at, datetime):
            return None

        exp_time = created_at + timedelta(seconds=self.session_duration)
        if datetime.utcnow() > exp_time:
            return None

        return session.user_id

    def destroy_session(self, request=None) -> bool:
        """Destroy a session based on the session ID in the request."""
        if not request:
            return False

        session_id = self.session_cookie(request)
        if not session_id:
            return False

        # Search and delete the session in the database
        session = UserSession.search({'session_id': session_id})[0]
        if not session:
            return False

        session.remove()
        return True
