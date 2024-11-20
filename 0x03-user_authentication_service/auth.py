#!/usr/bin/env python3
"""
A module for authentication-related routines.
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid


def _hash_password(password: str) -> bytes:
    """ Hash a password with bcrypt and return the salted hash in bytes.
    """
    password_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password_bytes, salt)

    return hashed_password


def _generate_uuid() -> str:
    """ Generates a new UUID and returns its string representation.
    """
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ Registers a new user in the database.
        """
        try:
            existing_user = self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_password = _hash_password(password)
            new_user = self._db.add_user(email, hashed_password)
            return new_user

    def valid_login(self, email: str, password: str) -> bool:
        """ Check if the provided email and password are valid.
        """
        try:
            user = self._db.find_user_by(email=email)
            if user:
                return bcrypt.checkpw(
                        password.encode('utf-8'), user.hashed_password
                        )
        except Exception:
            return False
        return False

    def create_session(self, email: str) -> str:
        """ Creates a session ID for a user identified by email.
        """
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except Exception:
            return None

    def get_user_from_session_id(self, session_id: str) -> User:
        """ Retrieve a User object based on a given session ID.
        """
        if not session_id:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except Exception:
            return None

    def destroy_session(self, user_id: int) -> None:
        """ Destroy the session for the given user by setting
        the session_id to None.
        """
        if user_id is None:
            return None
        self._db.update_user(user_id, session_id=None)

    def get_reset_password_token(self, email: str) -> str:
        """ Generate and return a reset password token for the given email.
        """
        try:
            user = self._db.find_user_by(email=email)
        except Exception:
            user = None

        if not user:
            raise ValueError()

        reset_token = _generate_uuid()
        self._db.update_user(user.id, reset_token=reset_token)

        return reset_token

    def update_password(self, reset_token: str, password: str) -> None:
        """ Update the user's password using a reset token.
        """
        try:
            user = self._db.find_user_by(reset_token=reset_token)
        except Exception:
            print("nice")
            raise ValueError()

        hashed_password = _hash_password(password)
        self._db.update_user(
                user.id,
                hashed_password=hashed_password,
                reset_token=None
        )
