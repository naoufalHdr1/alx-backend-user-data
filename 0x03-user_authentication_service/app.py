#!/usr/bin/env python3
"""
Set up a basic Flask app
"""
from flask import Flask, jsonify


app = Flask(__name__)


@app.route("/", methods=["GET"])
def hello():
    """ Returns a JSON response with a welcome message.
    """
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="5000")
