#!/usr/bin/env python3
"""
BasicAuth module to implement basic authentication mechanisms for the API.
"""
from api.v1.auth.auth import Auth
from models.user import User
import base64
from typing import TypeVar


class BasicAuth(Auth):
    """ Basic Authentication class inheriting from Auth """

    def extract_base64_authorization_header(
            self,
            authorization_header: str) -> str:
        """ Extracts the Base64 part of the Authorization header for
        Basic Authentication.
        """
        if authorization_header is None:
            return None

        if not isinstance(authorization_header, str):
            return None

        if not authorization_header.startswith("Basic "):
            return None

        # Directly slice to get the Base64 part after "Basic "
        return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """ Decodes the Base64 string base64_authorization_header.
        """
        if base64_authorization_header is None:
            return None

        if not isinstance(base64_authorization_header, str):
            return None

        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            return decoded_bytes.decode('utf-8')
        except (base64.binascii.Error, UnicodeDecodeError):
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """ Extracts the user email and password from the decoded Base64
        authorization header.
        """
        if decoded_base64_authorization_header is None:
            return (None, None)

        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)

        if ':' not in decoded_base64_authorization_header:
            return (None, None)

        email, password = decoded_base64_authorization_header.split(':')

        return email, password

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """ Retrieves the User instance based on the provided email and
        password.
        """
        if user_email is None or not isinstance(user_email, str):
            return None

        if user_pwd is None or not isinstance(user_email, str):
            return None

        try:
            # Try searching for user by email in the User database
            user = User.search({'email': user_email})
        except KeyError:
            return None

        # If no user is found with the provided email, return None
        if len(user) == 0:
            return None

        user = user[0]

        # Check if the password is valid
        if not user.is_valid_password(user_pwd):
            return None

        return user
