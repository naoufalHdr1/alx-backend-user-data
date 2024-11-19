#!/usr/bin/env python3
"""
A module for authentication-related routines.
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """ Hash a password with bcrypt and return the salted hash in bytes.
    """
    password_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password_bytes, salt)

    return hashed_password
