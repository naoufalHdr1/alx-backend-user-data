#!/usr/bin/env python3
"""
This module contains integration tests for the Flask application using
the `requests` module.
"""
import requests


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"
BASE_URL = "http://0.0.0.0:5000"


def register_user(email: str, password: str) -> None:
    """ Registers a new user with the given email and password.
    """
    data = {"email": email, "password": password}
    response = requests.post(f"{BASE_URL}/users", data=data)
    assert response.status_code == 200
    assert response.json() == {"email": EMAIL, "message": "user created"}


def log_in_wrong_password(email: str, password: str) -> None:
    """
    Attempts to log in with an incorrect password and validates the 401
    status code.
    """
    data = {"email": email, "password": password}
    response = requests.post(f"{BASE_URL}/sessions", data=data)
    assert response.status_code == 401


def log_in(email: str, password: str) -> str:
    """ Logs in with the correct credentials and returns the session ID.
    """
    data = {"email": email, "password": password}
    response = requests.post(f"{BASE_URL}/sessions", data=data)
    assert response.status_code == 200
    assert response.json() == {"email": email, "message": "logged in"}
    assert "session_id" in response.cookies
    return response.cookies["session_id"]


def profile_unlogged() -> None:
    """
    Attempts to access the profile route without being logged in,
    expecting a 403 status code.
    """
    response = requests.get(f"{BASE_URL}/profile")
    assert response.status_code == 403


def profile_logged(session_id: str) -> None:
    """
    Accesses the profile route while logged in and validates the returned
    email in the response.
    """
    cookies = {"session_id": session_id}
    response = requests.get(f"{BASE_URL}/profile", cookies=cookies)
    assert response.status_code == 200
    assert "email" in response.json()


def log_out(session_id: str) -> None:
    """
    Logs out using the session ID and validates the correct response status.
    """
    cookies = {"session_id": session_id}
    response = requests.delete(f"{BASE_URL}/sessions", cookies=cookies)
    assert response.status_code == 200
    assert response.json() == {"message": "Bienvenue"}


def reset_password_token(email: str) -> str:
    """
    Requests a password reset token for the given email and returns the token.
    """
    data = {"email": email}
    response = requests.post(f"{BASE_URL}/reset_password", data=data)
    assert response.status_code == 200
    assert response.json()["email"] == email
    assert "reset_token" in response.json()
    return response.json()["reset_token"]


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """ Updates the user's password using the reset token and new password.
    """
    data = {
            "email": email,
            "reset_token": reset_token,
            "new_password": new_password
    }
    response = requests.put(f"{BASE_URL}/reset_password", data=data)
    assert response.status_code == 200
    assert response.json() == {"email": email, "message": "Password updated"}


if __name__ == "__main__":

    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
