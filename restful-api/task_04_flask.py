#!/usr/bin/python3
"""A simple REST API built with Flask."""

from flask import Flask, jsonify, request


app = Flask(__name__)
users = {}


@app.route("/", methods=["GET"])
def home():
    """Welcome message."""
    return "Welcome to the Flask API!"


@app.route("/data", methods=["GET"])
def data():
    """Return the list of usernames."""
    return jsonify(list(users.keys()))


@app.route("/status", methods=["GET"])
def status():
    """Return API status."""
    return "OK"


@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    """Return a user by username or a 404 error."""
    user = users.get(username)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)


@app.route("/add_user", methods=["POST"])
def add_user():
    """Validate and add a new in-memory user."""
    user = request.get_json(silent=True)
    if not isinstance(user, dict):
        return jsonify({"error": "Invalid JSON"}), 400

    username = user.get("username")
    if not isinstance(username, str) or not username.strip():
        return jsonify({"error": "Username is required"}), 400
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = user
    return jsonify({"message": "User added", "user": user}), 201


if __name__ == "__main__":
    app.run()
