#!/usr/bin/env python3
"""
Set up a basic Flask app
"""
from flask import Flask, jsonify, request
from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route("/", methods=["GET"])
def hello():
    """ Returns a JSON response with a welcome message.
    """
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"])
def register_user():
    """
    Handles user registration.
    Returns:
    Response: A Flask JSON response with the following:
        - Success:
        {"email": "<email>", "message": "user created"}, status 200.
        - Error:
        {"message": "email already registered"}, status 400.
    """
    email = request.form.get("email")
    password = request.form.get("password")

    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="5000")
