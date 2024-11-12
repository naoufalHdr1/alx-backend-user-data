#!/usr/bin/env python3
"""
BasicAuth module to implement basic authentication mechanisms for the API.
"""
from api.v1.auth.auth import Auth


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
