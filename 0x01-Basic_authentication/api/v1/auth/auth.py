#!/usr/bin/env python3
""" Module that create an Authentication Class
"""
from flask import request
from typing import List, TypeVar


class Auth():
    """ Class to manage the API authentication
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Determines whether authentication is required for a given path.
        """
        return False

    def authorization_header(self, request=None) -> str:
        """ Retrieves the authorization header from the request.
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Retrieves the current user based on the request.
        """
        return None
