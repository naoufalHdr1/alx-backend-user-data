#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os
from api.v1.auth.auth import Auth


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

# Initialize `auth` based on `AUTH_TYPE`
auth = None
AUTH_TYPE = getenv("AUTH_TYPE")


if AUTH_TYPE == "basic_auth":
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()
elif AUTH_TYPE == "session_auth":
    from api.v1.auth.session_auth import SessionAuth
    auth = SessionAuth()
else:
    auth = Auth()


@app.before_request
def before_request():
    """Filter requests based on authentication requirements."""
    if auth is None:
        return

    excluded_paths = [
            '/api/v1/status/',
            '/api/v1/unauthorized/',
            '/api/v1/forbidden/'
            '/api/v1/auth_session/login/'
    ]

    # Check if request path needs authentication
    if not auth.require_auth(request.path, excluded_paths):
        return

    # Check for authorization header
    if (
            auth.authorization_header(request) is None and
            auth.session_cookie(request) is None
    ):
        abort(401, description="Unauthorized")

    request.current_user = auth.current_user(request)

    # Check for current user (authentication)
    if request.current_user is None:
        abort(403, description="Forbidden")


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized(error) -> str:
    """ Unauthorized handler
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """ Forbidden handler
    """
    return jsonify({"error": "Forbidden"}), 403


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
