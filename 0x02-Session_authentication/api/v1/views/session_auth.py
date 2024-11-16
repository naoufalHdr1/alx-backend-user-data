#!/usr/bin/env python3
"""
Module that handles all routes for the Session authentication.
"""
from api.v1.views import app_views
from flask import request, jsonify
from models.user import User
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def session_auth_login():
    """ Handles session authentication via login.
    """
    email = request.form.get('email')
    password = request.form.get('password')

    if not email:
        return jsonify({"error": "email missing"}), 400

    if not password:
        return jsonify({"error": "password missing"}), 400

    # Find user by email
    user = User.search({"email": email})[0]
    if not user:
        return jsonify({"error": "no user found for this email"}), 404

    # Check the user's password
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth
    session_id = auth.create_session(user.id)

    # Generate a response with the user's dictionary representation
    response = jsonify(user.to_json())

    # Set the session ID in the response cookie
    cookie_name = getenv('SESSION_NAME')
    response.set_cookie(cookie_name, session_id)

    return response


@app_views.route('/auth_session/logout',
                 methods=['DELETE'], strict_slashes=False)
def logout():
    """ Handles user logout by deleting the session.
    """
    from api.v1.app import auth
    if not auth.destroy_session(request):
        abort(404)
    return jsonify({}), 200
