#!/usr/bin/env python3
""" Module that create an Authentication Class
"""
from flask import request
from typing import List, TypeVar
import fnmatch
from os import getenv


class Auth():
    """ Class to manage the API authentication
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Determines whether authentication is required for a given path.
        """
        if path is None:
            return True

        if excluded_paths is None or len(excluded_paths) == 0:
            return True

        # Normalize paths by ensuring both have a trailing slash
        normalized_path = path if path.endswith('/') else path + '/'

        # Check if the normalized path is in excluded_paths
        for excluded_path in excluded_paths:
            normalized_excluded_path = (
                    excluded_path if excluded_path.endswith('/')
                    else excluded_path + '/'
            )
            # Use fnmatch to compare the paths, allowing wildcard matching
            if fnmatch.fnmatch(normalized_path, normalized_excluded_path):
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """ Retrieves the authorization header from the request.
        """
        if request is None:
            return None

        return request.headers.get('Authorization', None)

    def current_user(self, request=None) -> TypeVar('User'):
        """ Retrieves the current user based on the request.
        """
        return None

    def session_cookie(self, request=None):
        """ Retrieves the value of the session cookie from the request.
        """
        if request is None:
            return None

        # Get the cookie name from the environment variable
        cookie_name = getenv('SESSION_NAME')

        return request.cookies.get(cookie_name)
