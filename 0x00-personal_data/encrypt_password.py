#!/usr/bin/env python3
"""
Module for hashing and validating user passwords.
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hashes a password using bcrypt with a generated salt.
    """
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    return hashed_password


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Validates that the provided password matches the stored hashed password.
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
